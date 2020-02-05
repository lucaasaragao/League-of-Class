from django import forms
from .models import Professor
from .models import Aluno



class ProfessorForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo de formulario a partir do modelo que esta sendo criado no db;
	'''
	class Meta:
		model = Professor
		fields = '__all__'


'''
class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
'''
