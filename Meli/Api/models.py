from django.db import models

'''class Test2(models.Model):
    name = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
'''

class DNA(models.Model):
    dna = models.CharField(max_length=200,unique=True)
    isMutant = models.BooleanField()
    dateLastRequest = models.DateField(auto_now=True)