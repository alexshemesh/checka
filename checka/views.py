from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from rest_framework import generics
from . models import PaymentCheck,Shop
from . forms import CheckForm
from . serializers import CheckSerializer, ShopSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    """The home page for k8s cleaner operations"""
    return render(request, 'checka/index.html')

@login_required
def checks(request):
    """Show all topic"""
    checks = PaymentCheck.objects.order_by('date_added')
    context = {'checks': checks }
    return render(request, 'checka/checks.html', context )

@login_required
def check(request, check_id):
    """Show a single topix and all its entries"""
    check = PaymentCheck.objects.get(id=check_id)
    context = {'check': check }
    return render(request, 'checka/check.html', context)

@login_required
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

@login_required
def edit_check(request, check_id):
        """Edit an existing check."""
        check = PaymentCheck.objects.get(id=check_id)

        if request.method != 'POST':
            form = CheckForm(instance=check)
        else:
            # POST data submitted; process data.
            form = CheckForm(instance=check, data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('checka:checks'))

        context = {'check': check,  'form': form}
        return render(request, 'checka/edit_check.html', context)

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PaymentCheck.objects.all()
    serializer_class = CheckSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new check."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = PaymentCheck.objects.all()
    serializer_class = CheckSerializer

class CreateShopView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new check."""
        serializer.save()


class DetailsShopView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


