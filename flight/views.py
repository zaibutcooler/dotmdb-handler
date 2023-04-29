from django.shortcuts import render

# Create your views here.

def flightindex(request):
	data={}
	return render(request,"flight/flightindex.html",data)