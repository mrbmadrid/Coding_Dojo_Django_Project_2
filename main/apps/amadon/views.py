# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	if not 'quantity_purchased' in request.session:
		request.session['quantity_purchased'] = 0
	if not 'total_cost' in request.session:
		request.session['total_cost'] = 0
	global products
	products = [
		["Dojo Tshirt" , 19.99],
		["Dojo Sweater" , 29.99],
		["Dojo Cup" , 4.99],
		["Algorithm Book" , 49.99]
	]
	request.session['products'] = products
	return render(request, "amadon/index.html")

def success(request):
	return render(request, "amadon/success.html")

def purchase(request):
	quantities = [int(request.POST['Dojo Tshirt']), int(request.POST['Dojo Sweater']), int(request.POST['Dojo Cup']), int(request.POST['Algorithm Book'])]
	request.session['current_cost'] = 0
	for idx, number in enumerate(quantities):
		request.session['quantity_purchased'] += number
		request.session['total_cost'] += number * products[idx][1]
		request.session['current_cost'] += number * products[idx][1]
	return redirect(success)