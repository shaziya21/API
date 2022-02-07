from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentRegistration
from .models import StudentInfo


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = StudentInfo(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect(reverse('add'))
    else:
        fm = StudentRegistration()
    Stud = StudentInfo.objects.all()
    return render(request, 'enroll/addshow.html', {'form': fm, 'stuinfo': Stud})


def update_data(request, id):
    person = StudentInfo.objects.get(pk=id)
    fm = StudentRegistration(instance=person)

    if request.method == 'POST':
        fm = StudentRegistration(request.POST, instance=person)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('add'))
    else:
        return render(request, 'enroll/update.html', {'form': fm})


def delete_data(request, id):
    person = StudentInfo.objects.get(pk=id)
    if request.method == 'POST':
        person.delete()
        return HttpResponseRedirect(reverse('add'))
    else:
        return render(request, 'enroll/delete.html', {'object': person})
