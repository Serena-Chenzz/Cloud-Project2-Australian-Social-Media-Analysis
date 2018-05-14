from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('hours/', views.hourly_data),
]


urlpatterns += [
    path('weekdays/', views.week_days_data),
]

urlpatterns += [
    path('total_sentiment/', views.total_sentiment),
]


urlpatterns += [
    path('per_area/', views.per_area),
]

urlpatterns += [
    path('areas/', views.areas),
]

urlpatterns += [
    path('areas_polarity/', views.areas_polarity),
]
