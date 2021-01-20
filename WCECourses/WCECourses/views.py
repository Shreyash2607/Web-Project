import os
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.base import View

class landingPage(View):
    
    def get(self, request, template_name='landingPage.html'):
        return render(request, template_name)