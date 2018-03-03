# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class TipoPersona (models.Model):
    descr=models.CharField('Tipo',max_length=255)
  
    class Meta:
        ordering = ('descr',)
    
    def __unicode__(self):
        return self.descr 
    
class TipoCompetenza (models.Model):
    descr=models.CharField('Competenza',max_length=255)
    
    def __unicode__(self):
        return self.descr 
        
class Persona(models.Model):
    class Meta:
        ordering=['cognome','nome']
    titolo=models.CharField('Titolo',max_length=20,null=True,blank=True)
    nome = models.CharField(max_length=50,null=False,blank=False)
    cognome = models.CharField(max_length=50,null=False,blank=False)
    cf=models.CharField('Codice Fiscale',max_length=16,null=True,blank=True)
    dataNascita=models.DateTimeField('Data Nascita',null=True,blank=True)
    luogocomune=models.ForeignKey('GestioneRiferimenti.Comune',verbose_name='Comune di nascita',default=None,null=True,blank=True)
    tipo=models.ManyToManyField('TipoPersona',null=False,blank=False)
    competenza=models.ManyToManyField('TipoCompetenza',blank=True)
    lavoratoap=models.BooleanField('Gia'' lavorato con AP',default=False)
    strutturaSoggetto=models.ManyToManyField('GestioneIncarichi.StrutturaSoggetto',through='GestioneIncarichi.IncaricoIstituzionale',blank=True)
    note=models.TextField('Nota',null=True,blank=True)
    dataAgg=models.DateTimeField('Data Aggiornamento',default=timezone.now)
    provincia=models.ForeignKey('GestioneRiferimenti.Provincia',default=None,null=True,blank=True)
    regione=models.ForeignKey('GestioneRiferimenti.Regione',default=None,null=True,blank=True)
        
    def __unicode__(self):
        return self.cognome+' '+self.nome        
    

    
    