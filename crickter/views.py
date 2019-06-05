from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Msg
# Create your views here.

def home(request):
	template_name = "crickter/main.html"
	queryset = Msg.objects.all().order_by('-timestamp')
	context = {
		"objects": queryset
	}
	if request.method == "POST":
		name = request.user
		msg = request.POST.get("msg")
		obj = Msg.objects.create(
			user = name,
			name = name,
			msg = msg
			)
	return render(request, template_name, context)


def add(request):
	template_name = "crickter/form.html"
	if request.method == "POST":
		# name = request.POST.get("name")
		name = request.user
		msg = request.POST.get("msg")
		obj = Msg.objects.create(
			user = name,
			name = name,
			msg = msg
			)
		return HttpResponseRedirect("/")
	context= {}
	return render(request, template_name, context)

def info(request):
	template_name = "crickter/info.html"
	user = None
	if request.user.is_authenticated():
		user = Msg.objects.filter(user=request.user).order_by('-timestamp')
	context = {"objects" : user}
	return render(request, template_name, context)	
