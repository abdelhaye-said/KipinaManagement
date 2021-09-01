from re import M
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Enfant(models.Model):
    TYPE=(
        ('exterieur','exterieur'),
        ('interne','interne'),
    )
    CLASSE=(
        ('Foxes','Foxes'),  
        ('Little-Foxes','Little-Foxes'),
        ('Bears','Bears'),
        ('Seals','Seals'),
        ('Owls','Owls'),
    )
    name=models.CharField(max_length=100, null=True)
    prenom=models.CharField(max_length=100, null=True)
    nationalite=models.CharField(max_length=100, null=True)
    langueMaternelle=models.CharField(max_length=100, null=True)
    langueParlee=models.CharField(max_length=100, null=True)
    type=models.CharField(max_length=100, null=True, choices=TYPE)
    date_naissance=models.CharField(max_length=100, null=True)
    date_inscription=models.DateTimeField(auto_now_add=True)
    claSSe=models.CharField(max_length=100, null=True, choices=CLASSE)
    frais_scolarite=models.BooleanField()
    
    def __str__(self):
        return self.name



class Assurance(models.Model):
    TYPE=(
        ('OUI','OUI'),
        ('NON','NON'),
    )
    enfant=models.ForeignKey(Enfant,null=True, on_delete=models.SET_NULL)
    assure=models.CharField(max_length=100, null=True, choices=TYPE)

    def __str__(self):
        return self.assure

class Cantine(models.Model):
    TYPE=(
        ('4j','4j'),
        ('5j','5j'),
        ('NON','NON'),
    )
    enfant=models.ForeignKey(Enfant,null=True, on_delete=models.SET_NULL)
    type_cantine=models.CharField(max_length=100, null=True, choices=TYPE)

    def __str__(self):
        return self.type_cantine

class Transport(models.Model):
    TYPE_TRANS=(
        ('AM','AM'),
        ('PM','PM'),
        ('AM-PM','AM-PM'),
        ('NON','NON'),
    )

    enfant=models.ForeignKey(Enfant,null=True, on_delete=models.SET_NULL)
    type_transport=models.CharField(max_length=100, null=True, choices=TYPE_TRANS)

    def __str__(self):
        return self.type_transport
class Service_Garde(models.Model):
    TYPE_GARDE=(
        ('AM','AM'),
        ('PM','PM'),
        ('AM-PM','AM-PM'),
        ('Mercredi PM','Mercredi PM'),
        ('NON','NON'),
    )

    enfant=models.ForeignKey(Enfant,null=True, on_delete=models.SET_NULL)
    type_garde=models.CharField(max_length=100, null=True, choices=TYPE_GARDE)

    def __str__(self):
        return self.type_garde

class Forfait(models.Model):
    TYPE_FORFAIT=(
        ('journee-complte','journee-complte'),
        ('demi-journee-matinee','demi-journee-matinee'),
        ('demi-journee-apres-midi','demi-journee-apres-midi'),
        ('2-jours-par-semaine','2-jours-par-semaine'),
    )

    enfant=models.ForeignKey(Enfant,null=True, on_delete=models.SET_NULL)
    type_forfait=models.CharField(max_length=100, null=True, choices=TYPE_FORFAIT)

    def __str__(self):
        return self.type_forfait




