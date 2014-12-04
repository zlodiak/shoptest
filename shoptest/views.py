# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response

from shoptest.models import Book


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
	t = loader.get_template('custom_products.html')
	c = RequestContext(request, {
		'object_list': Book.objects.all(),
	})	
	
	return HttpResponse(t.render(c)) 		

