from django.db import models

class Filmes:
    diretor  = models.CharField(max_length=50)
    titulo = models.CharField(max_length=255)
    AnoLançamento = models.CharField(max_length=4)
    classificacao = models.CharField(max_length=10)
    sinopse = models.TextField()
    
    def __str__(self):
        return self.title