from django.shortcuts import render

# Create your views here.
def home_page():
	return HttpResponse('<html><title>To-Do lists</title></html>')
