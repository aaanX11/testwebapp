# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Supply, UserPerson, UserSuggestion, FoodType, FoodInstance
from .forms import SupplyForm, SuggestionForm
from django.shortcuts import render, redirect

def suggestion(request):
    if request.method == "POST":
        pass
    else:
        pass
#        return render(request, 'ggame/riddleshow.html',{'riddle':riddle, 'form':form})


def supply(request, pk):
    supply=Supply.objects.get(pk=pk)
    instances=FoodInstance.objects.filter(supply=supply)
    return render(request, 'foodsharing/supply.html',{'supply':supply, 'instances':instances})

def list_supplies(request):
    supplies=Supply.objects.all()[:20]
    return render(request, 'foodsharing/list_sup.html', {'supplies':supplies})

def list_users(request):
    users=UserPerson.objects.all()[:20]
    return render(request, 'foodsharing/list_users.html', {'users':users})

 
def list_suggestions(request):
    suggestions=UserSuggestion.objects.all()[:20]
    return render(request, 'foodsharing/list_sug.html', {'suggestions':suggestions})


