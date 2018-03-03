# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Struttura(models.Model):
    organo=models.CharField('Organo/Area',max_length=255)
    ruolo=models.CharField('Ruolo',max_length=255)
    tipo=models.CharField('Tipo',max_length=20)
    nota=models.TextField('Nota',max_length=1000,null=True,blank=True)
    
    
    def __unicode__(self):
        return self.organo+' - '+self.ruolo

class Delega(models.Model):
    descr=models.CharField('Descrizione/Delega',max_length=255)
    nota=models.TextField('Nota',max_length=1000,null=True,blank=True)
   
    def __unicode__(self):
        return self.descr

class StrutturaSoggetto(models.Model):
    soggetto=models.ForeignKey('GestioneSoggetti.Soggetto',blank=True,null=True)
    struttura=models.ForeignKey('Struttura',blank=True,null=True,verbose_name="Organo Ruolo")
    delega=models.ForeignKey("Delega",blank=True,null=True)
    dataAgg=models.DateTimeField('Data Aggiornamento',default=timezone.now)
    dataini=models.DateField("da",default=timezone.now,null=False,blank=False)
    datafin=models.DateField("a",default=None,null=True,blank=True)
    SI=1
    NO=0
    SINO=(
          (SI,'Sì'),
          (NO,'No'),    
          )
    
    rappleg=models.IntegerField('Rappresentante Legale',choices=SINO,default=NO)
    nota=models.TextField('Nota',max_length=1000,null=True,blank=True)
    
    def __unicode__(self):
        if  self.delega is None:
            #return self.soggetto.denominazione+' '+'' if self.struttura.organo==None else self.struttura.organo+' '+'' if self.struttura.ruolo==None else self.struttura.ruolo+' senza delega '
            return self.soggetto.denominazione+' '+self.struttura.organo+' '+self.struttura.ruolo+' senza delega '
        else:
            #return self.soggetto.denominazione+' '+'' if self.struttura.organo==None else self.struttura.organo+' '+ '' if self.struttura.ruolo==None else self.struttura.ruolo+' con delega '+'' if self.delega.descr==None else self.delega.descr
            return self.soggetto.denominazione+' '+self.struttura.organo+' '+ self.struttura.ruolo+' con delega '+self.delega.descr
class IncaricoIstituzionale(models.Model):
    strutturasoggetto=models.ForeignKey('StrutturaSoggetto')
    persona=models.ForeignKey('GestionePersone.Persona')
    SI=1
    NO=0
    SINO=(
          (SI,'Sì'),
          (NO,'No'),    
          )
    refpol=models.IntegerField('Referente Politico',choices=SINO,default=NO)
    reftec=models.IntegerField('Referente Tecnico',choices=SINO,default=NO)
    dataAgg=models.DateTimeField('Data Aggiornamento',default=timezone.now)
    dataini=models.DateField("da",default=timezone.now,null=False,blank=False)
    datafin=models.DateField("a",default=None,null=True,blank=True)
    nota=models.TextField('Nota',max_length=1000,null=True,blank=True)
    
    def __unicode__(self):
        return self.persona.cognome+' '+self.persona.nome+' '+self.strutturasoggetto.soggetto.denominazione +' '+self.strutturasoggetto.struttura.organo+' '+self.strutturasoggetto.struttura.ruolo+' '+'' if self.strutturasoggetto.delega is None else self.strutturasoggetto.delega.descr 
    