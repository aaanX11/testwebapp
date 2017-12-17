# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Supply, UserPerson, UserSuggestion, FoodType, FoodInstance
from .forms import SupplyForm, SuggestionForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.core import serializers


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def suggestion(request):
    if request.method == "POST":
        pass
    else:
        pass
def home(request):
    supplies=Supply.objects.all()[:20]
    if request.is_ajax():
        data = serializers.serialize('json', Supply.objects.all()[:20], use_natural_foreign_keys=True)
        return HttpResponse(data)    
    return render(request, 'foodsharing/list_map_ajax.html',{'supplies':supplies}) 

def supply(request, pk):
    supply=Supply.objects.get(pk=pk)
    instances=FoodInstance.objects.filter(supply__id=pk)
    return render(request, 'foodsharing/supply.html',{'supply':supply, 'instances':instances})

def list_supplies(request):
    supplies=Supply.objects.all()[:20]
    return render(request, 'foodsharing/list_sup.html', {'supplies':supplies})

def list_users(request):
    if request.user.is_authenticated:
        #users=UserPerson.objects.all()[:20]
        #return render(request, 'foodsharing/list_users.html', {'users':users})
        print('authenticated')
    else:
        print('not authenticated')
        #return redirect('/home')
    users=UserPerson.objects.all()[:20]
    return render(request, 'foodsharing/list_users.html', {'users':users})


def user(request, pk):
    user=UserPerson.objects.get(pk=pk)
    suggestions=UserSuggestion.objects.filter(user_id__id=pk)
    return render(request, 'foodsharing/user.html',{'user':user, 'suggestions':suggestions})


def list_suggestions(request):
    suggestions=UserSuggestion.objects.all()[:20]
    return render(request, 'foodsharing/list_sug.html', {'suggestions':suggestions})


def sugg_form(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = SuggestionForm()
    return render(request, 'foodsharing/sugg_form.html', {'form': form})

def supp_form(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
             
    else:
        form = SupplyForm()
    return render(request, 'foodsharing/supp_form.html', {'form': form})


