# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	if not request.session['words']:
		request.session['words']=[]
	return render(request, 'session_words/index.html')

def submit(request):
	data = request.session['words']
	data.append({'word':request.POST['word'], 'classes':request.POST['color'] + (" big" if (request.POST.get('big', '')=='big') else "")})
	request.session['words']=data;
	return redirect(index)

def clear(request):
	request.session['words']=[]
	return redirect(index)
