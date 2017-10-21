# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Riddle, RiddleShow
from .forms import RiddleForm
from django.shortcuts import render, redirect

# Create your views here.

def riddleshow(request):
    if request.method == "POST":
        form=RiddleForm(request.POST)
        if form.is_valid():
            form.clean()
            return redirect('game')
            
    else:
        form = RiddleForm()
        riddle = Riddle.objects.all().first()
        return render(request, 'ggame/riddleshow.html',{'riddle':riddle, 'form':form})

def game(request):
    return render(request, 'ggame/game.html')
