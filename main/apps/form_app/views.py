# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	return render(request, "form_app/index.html")

def success(request):
	return render(request, "form_app/success.html")

def submit(request):
	if not 'times' in request.session:
		request.session['times'] = 0
	request.session['times'] += 1
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['favorite'] = request.POST['favorite']
	request.session['comment'] = request.POST['comment']
	return redirect(success)