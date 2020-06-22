from django.shortcuts import render
from .models import Applicant, Application
from .forms import ApplicantForm, ApplicationForm
from django.http import HttpResponseRedirect, HttpResponse
from django import forms


# Create your views here.

def index(request):
    all_apps = Application.objects.all()
    context = {'all_apps': all_apps}
    return render(request, 'index.html', context)


def apply(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ApplicantForm()

    return render(request, 'apply.html', {'form': form})


def new_app(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ApplicationForm()

    return render(request, 'newapp.html', {'form': form})
