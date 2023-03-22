from django.shortcuts import redirect, render

from view.forms import reportForm


def index(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contect/contect.html')


def report(request):
    if request.POST:
        form = reportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'report/report.html', {'form': reportForm})
