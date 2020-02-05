from django.shortcuts import render

# Create your views here.


def home(request):
	#pagina inicial do league of class;
	return render(request,'home.html');