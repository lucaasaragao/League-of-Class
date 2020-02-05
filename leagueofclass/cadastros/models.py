from django.db import models
import datetime
# Create your models here.
# Responsavel por criar os models do cad de professor e aluno


class Cpf(models.Model):
	numeroCPF=models.CharField(max_length=14)
	pessoa = models.OneToOneField("Pessoa",on_delete=models.CASCADE)



class Pessoa(models.Model):
		options_sexo=(('M','Masculino'),('F','Feminino'),('NDA','Qualquer Outro'))
		nome=models.CharField(max_length=60)
		sexo=models.CharField(max_length=1,choices=options_sexo)
		dataNascimento=models.DateField(("Data"), default=datetime.date.today)
		email=models.CharField(max_length=50)
		login=models.CharField(max_length=20)
		password=models.CharField(max_length=20);


class Professor(Pessoa):
	nomeInstituicao=models.CharField(max_length=30, primary_key=True)
	codigo=models.CharField(max_length=10)
	matricula=models.CharField(max_length=20)


class Aluno(Pessoa):
	nomeInstituicao=models.CharField(max_length=30,primary_key=True)
	descricaoDesempenho=models.CharField(max_length=150)
	frequencia=models.CharField(max_length=40)
	professor=models.ManyToManyField("Professor");



class Notas(models.Model):
	primeiraUnidade=models.CharField(max_length=4)
	segundaUnidade=models.CharField(max_length=4)
	terceiraUnidade=models.CharField(max_length=4)
	media=models.CharField(max_length=4)

class Disciplinas(models.Model):
	nomeDisciplina=models.CharField(max_length=30)
	descricaoDisciplina=models.CharField(max_length=120)
	professor = models.ForeignKey("Professor",on_delete=models.CASCADE)
	aluno = models.ForeignKey("Aluno",on_delete=models.CASCADE)






