from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
#Count used for aggregate counts - .count also an option when just counting something within one table
from django.db.models import Count
# CONTROLLER!!!
# Create your views here.
def index(request):
	#using loginandreg instead of belt_review allows me to pull in html files from other app
	return render(request, 'user_dashboard/index.html')
