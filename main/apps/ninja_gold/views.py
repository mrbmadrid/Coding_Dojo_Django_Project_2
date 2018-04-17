# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from random import random
from django.http import JsonResponse
# Create your views here.

def index(request):
	if not 'gold' in request.session:
		request.session['gold']=0
	return render(request, "ninja_gold/index.html")

def ninjado(request, action):
	if action == 'farm':
		request.session['current'] = int(random()*11)+10
		request.session['gold'] += request.session['current']
	elif action == 'cave':
		request.session['current'] = int(random()*6)+5
		request.session['gold'] += request.session['current']
	elif action == 'casino':
		request.session['current'] = int(random()*101)-50
		request.session['gold'] += request.session['current']
	elif action == 'house':
		request.session['current'] = int(random()*3)+2
		request.session['gold'] += request.session['current']
	data = {'gold':request.session['gold'], 'current':request.session['current']}
	return JsonResponse(data, status=201)

