from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from .forms import CreateList

def index(request):
    return HttpResponse('Hello World')

def create(response):
	if response.method == "POST":
		form = CreateList(response.POST)
		if form.is_valid():
			n = form.cleaned_data["name"]
			t = List(name=n)
			t.save()
			response.user.list.add(t)	
	else:
		form = CreateList()
	return render(response, "ProjectApp/create.html", {"form": form})

# Create your views here.
