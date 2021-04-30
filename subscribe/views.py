from django.shortcuts import render

from .models import SubscribeUser
from .forms import SubscribeUserSignUpForm
# Create your views here.

def subscibe_signup(request):
    form = SubscribeUserSignUpForm(request.POST or None)

    if form.is_valid():
        isinstance = form.save(commit=False)
        if SubscribeUser.objects.filter(email=isinstance.email).exists():
            print("Email is already exist!")
        else: 
            isinstance.save()

    context = {
        'form': form,
    }
    template = 'subscribe/subscribe.html'

    return render(request, template, context)

