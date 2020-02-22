from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def index(request):
    """return the index.html file """
    return render(request, 'index.html')

def logout(request):
    """ log out the user """
    auth.logout(request)
    return redirect(reverse('index'))
