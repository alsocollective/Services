from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
import json,re



def ip(request):
	data = json.dumps({"host": request.META.get('REMOTE_ADDR')})
	data = "%s(%s);"%(request.META['PATH_INFO'].split("/")[-1].split("=")[1],data)

	return HttpResponse(data, mimetype='application/json',content_type="application/json")

	