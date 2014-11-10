from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import simplejson


def ip(request):
	data = simplejson.dumps({"host": request.META.get('REMOTE_ADDR')})
	return HttpResponse(data, mimetype='application/json')

