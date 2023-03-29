from django.urls import path
from view.views import StationAll, TrackingID, about, Station, index, report

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', Station, name="contact"),
    path('report/', report, name="report"),
    path('stations/', StationAll, name="station"),
    path('tracking/', TrackingID, name="tracking")
]
