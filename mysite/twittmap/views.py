from django.shortcuts import render

# Create your views here.
from .models import Tweet

def index(request):
	return render(request, 'twittmap/index.html')