from django.urls import path
from view.views import about, contact, index, report

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('report/', report, name="report")
]
