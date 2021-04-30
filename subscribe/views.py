from django.shortcuts import render

from .models import SubscribeUser
from .forms import SubscribeUserSignUpForm
# Create your views here.

def view_subscribe(request):
    """ A view that renders the bag contents page """

    return render(request, 'subscribe/subscribe.html')

def subscibe_signup(request):
    form = SubscribeUserSignUpForm(request.POST or None)
    if form.is_valid():
        form = SubscribeUserSignUpForm(request.POST)
        if SubscribeUser.objects.filter(email=instance.email).exists():
            print("Email is already exist!")
        else:
            instance.save()

    context = {
        'form': form,
    }
    return render(request, context)
