from django.shortcuts import render
from .models import Aluno,Professor
from .form import ProfessorForm;
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
# Create your views here.



def cad(request):
	#url cadastro/ retorna o template de cadastros Professor!
	#Ñ implementada ainda;
	
	if request.method=="POST":
		form = ProfessorForm(request.POST)

		if form.is_valid():
			n1 = form.save();
			response = redirect('/home')
			return response

	else:
		form = ProfessorForm()

	return render(request,'cadastroProfessor.html', {'form':form});


def cadAluno(request):
	pass
