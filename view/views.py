from django.shortcuts import redirect, render

from view.forms import reportForm
from view.models import ReportModel, StationModel


def index(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'about/about.html')


def Station(request):
    return render(request, 'contect/contect.html')


def report(request):
    if request.POST:
        form = reportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'report/report.html', {'form': reportForm})


def StationAll(request):
    return render(request, 'station/stationList.html', {'station': StationModel.objects.all()})


def TrackingID(request):
    if request.POST:

        data = ReportModel.objects.filter(ID=request.POST.get('id')).first()

        return render(request, 'tracking/tracking.html', {'data': data, 'message': True})

    else:
        return render(request, 'tracking/tracking.html', {'message': False})
