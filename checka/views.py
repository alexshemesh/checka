from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . models import Check
from . forms import CheckForm


def index(request):
    """The home page for k8s cleaner operations"""
    return render(request, 'checka/index.html')


def checks(request):
    """Show all topic"""
    checks = Check.objects.order_by('date_added')
    context = {'checks': checks }
    return render(request, 'checka/checks.html', context )


def check(request, check_id):
    """Show a single topix and all its entries"""
    check = Check.objects.get(id=check_id)
    context = {'check': check }
    return render(request, 'checka/check.html', context)



def new_check(request):
    if request.method != 'POST':
        form = CheckForm()
    else:
        form = CheckForm(data=request.POST,files=request.FILES)
        print("wtf")
        if form.is_valid():
            print("wtf valid")
            form.save()
            return HttpResponseRedirect(reverse('checka:checks'))
        else:
            messages.error(request, "Error")
    context = {'form': form }
    return render(request, 'checka/new_check.html', context)