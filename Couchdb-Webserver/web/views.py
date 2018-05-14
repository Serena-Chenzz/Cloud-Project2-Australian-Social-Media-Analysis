from django.http import JsonResponse
from django.shortcuts import render
import couchdb
from django.conf import settings


db_servers_address = settings.COUCHDB_SERVERS

# couchserver = couchdb.Server("http://115.146.86.136:5986/")
#
# db = couchserver['tweet']
dbs = [couchdb.Server(db_address)['tweet'] for db_address in db_servers_address]


time_view_doc = 'time_data'
hours_view = 'hours'
week_days_view = 'week_days'


sentiment_view_doc = 'sentiment'
total_sentiment_view = 'total_sentiment'


area_view = 'sa2_data'
area_sentiment_view = 'sa2_sentiment'


def index(request):
    return render(request, 'index.html')



def hourly_data(request):
    resp = {}
    for db in dbs:
        try:
            rows = db.view(time_view_doc + '/' + hours_view, group=True, stale='ok')
            for row in rows:
                resp[row.key] = row.value
            break
        except Exception as e:
            pass
    return JsonResponse(resp, safe=False)


def week_days_data(request):
    resp = {}
    for db in dbs:
        try:
            rows = db.view(time_view_doc + '/' + week_days_view, group=True, stale='ok')
            resp = {}
            for row in rows:
                resp[row.key] = row.value
            break
        except Exception as e:
            pass
    return JsonResponse(resp, safe=False)


def total_sentiment(request):
    resp = {}
    for db in dbs:
        try:
            rows = db.view(sentiment_view_doc + '/' + total_sentiment_view, group=True, stale='ok')
            resp = {}
            for row in rows:
                resp[row.key] = row.value
            break
        except Exception as e:
            pass
    return JsonResponse(resp, safe=False)

def per_area(request):
    resp = {}
    for db in dbs:
        try:
            rows = db.view(area_view + '/' + area_sentiment_view, group=True, stale='ok')
            resp = {"rows": []}
            for row in rows:
                resp["rows"].append({"key": row['key'], "value": row['value']})
            break
        except Exception as e:
            pass
    return JsonResponse(resp,safe=True)

def areas(request):
    resp = {}
    for db in dbs:
        try:
            resp = db['1234567890']
            break
        except Exception as e:
            pass
    return JsonResponse(resp, safe=True)


def areas_polarity(request):
    resp = {}
    for db in dbs:
        try:
            header, resp = db.list("sa2_data/polarity_per_area","sa2_data/sa2_sentiment",stale='ok',reduce='false')
            break
        except Exception as e:
            pass
    return JsonResponse(resp, safe=True)
