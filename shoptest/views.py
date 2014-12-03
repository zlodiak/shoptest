# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response


def index(request):
	"""
	handler for main
	"""		
	t = loader.get_template('index.html')
	c = RequestContext(request, {})	
	
	return HttpResponse(t.render(c)) 		


def contacts(request):
	"""
	handler for contacts
	"""		
	t = loader.get_template('contacts.html')
	c = RequestContext(request, {})	
	
	return HttpResponse(t.render(c)) 		


def custom_products(request):
	"""
	handler for custom_products
	"""		
	print(12)
	t = loader.get_template('custom_products.html')
	c = RequestContext(request, {})	
	
	return HttpResponse(t.render(c)) 		

