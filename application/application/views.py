from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
import json,re,requests


def allother(request):
	out = """
		<h1>ALSO Services</h1>
		<a href="http://alsocollective.com">did you mean to go to our main site?</a>
		<br>
		<br>
		<p>if requesting content from this site either go to /loc or /ip</p>
		<p>both of the services are require to be quired with a callback functoin</p>
		<code>
		$.getJSON("http://examplewebsite.com/ip/&callback=?", function(data){ <br>
			console.log(data);	<br>
			GLOBAL.getLocation(data.host); <br>
		});
		</code>
		<h2>/loc</h2>
		<p>returns your location in a json</p>
		<h2>/ip</h2>
		<p>returns your IP address</p>
	"""
	return HttpResponse(out)

# We simply return the users ip addres to them as a function
# this requires a call back, example bellow
'''
$.getJSON("http://examplewebsite.com/ip/&callback=?", function(data){
	console.log(data);	
	GLOBAL.getLocation(data.host);
});
'''
def ip(request):
	data = json.dumps({"host": request.META.get('REMOTE_ADDR')})
	data = "%s(%s);"%(request.META['PATH_INFO'].split("/")[-1].split("=")[1],data)

	return HttpResponse(data, mimetype='application/json',content_type="application/json")

# same as above but instead sends the country back, all in one call instead of 2...
# requires the call back as well
def country(request):
	# ip = "135.23.138.145"
	ip = request.META.get('REMOTE_ADDR')
	r = requests.get('http://api.ipinfodb.com/v3/ip-country/?key=d041a5c794a07541210c9595ec4434afbf90a14b46f568b38666562071740435&ip=%s&format=json'%ip)
	return HttpResponse("%s(%s);"%(request.META['PATH_INFO'].split("/")[-1].split("=")[1],r.text), mimetype='application/json',content_type="application/json")