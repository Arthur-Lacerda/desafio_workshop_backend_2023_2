from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=20)
    objetivo = models.CharField(max_length=100)
        
    def __str__(self):
            return f"Nome: {self.nome} & Objetivo do projeto: {self.objetivo}"
    

class Grupo(models.Model):
      projeto = models.ForeignKey(
            Projeto, 
            max_length=120,
            on_delete=models.CASCADE,
            help_text="Selecione qual projeto você deseja relacionar com esse grupo",
      )
      choices_status = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
      veteranos = models.CharField(choices = choices_status, max_length = 1)
      PO = models.CharField(max_length=50, help_text='Nome e Sobrenome',verbose_name= "Product Owner: ")
      backEnd1 = models.CharField(max_length=50, help_text='Nome e Sobrenome',verbose_name= "1° Backend: ")
      backEnd2 = models.CharField(max_length=50, help_text='Nome e Sobrenome', blank=True,verbose_name= "2° Backend(opcional): ")
      backEnd3 = models.CharField(max_length=50, help_text='Nome e Sobrenome', blank=True,verbose_name= "3° Backend(opcional): ")
      frontEnd = models.CharField(max_length=50,verbose_name= "Front End: ",help_text='Nome e Sobrenome')
