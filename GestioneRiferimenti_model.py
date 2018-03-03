from django.db import models

class TipoSede (models.Model):
    descr=models.CharField('Sede',max_length=255)
    

    def __unicode__(self):
        return self.descr 

class TipoIndirizzo (models.Model):
    descr=models.CharField('Tipo',max_length=255)
    
    def __unicode__(self):
        return self.descr    



class Comune(models.Model):
    class Meta:
        ordering=['descrizione']

    descrizione=models.CharField(max_length=255)
    codComune=models.CharField(max_length=3)
    codProvincia=models.CharField(max_length=3)
    codRegione=models.CharField(max_length=2)
    codIstat=models.CharField(max_length=8)
    regione=models.CharField(max_length=255)
    provincia=models.CharField(max_length=255)
    popolazione=models.IntegerField()
    riparGeo=models.CharField(max_length=255)
    CodRipartGeo=models.SmallIntegerField()
    capoluogo=models.SmallIntegerField()
    sigla=models.CharField(max_length=5)
    def __unicode__(self):
        return self.descrizione
    
class Provincia(models.Model):
    class Meta:
        ordering=['descrizione']
    descrizione=models.CharField(max_length=255)
    regione=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.descrizione

class Regione(models.Model):
    class Meta:
        ordering=['descrizione']
    descrizione=models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.descrizione

class Riferimento(models.Model):
    soggetto=models.ForeignKey("GestioneSoggetti.Soggetto",related_name='rifSoggetto',blank=True,null=True)
    persona=models.ForeignKey("GestionePersone.Persona",related_name='rifPersona',blank=True,null=True)
    strutturaSoggetto=models.ForeignKey("GestioneIncarichi.StrutturaSoggetto",related_name='rifStrutturaSoggetto',blank=True,null=True)
    incaricoIst=models.ForeignKey("GestioneIncarichi.IncaricoIstituzionale",related_name='rifIncaricoIstituzionale',blank=True,null=True)

class Email(Riferimento):
    tipoEmail=(
                (None, 'Selezionare tipo email'),
                ( 'std','Standard'),
                ('pec','PEC')
                )   
    tipo=models.CharField('Tipo Email',max_length=3,choices=tipoEmail)
    address=models.EmailField('Email',max_length=100);
    tipoSede=models.ForeignKey("TipoSede",related_name='tiposedeEmail')

class Account(Riferimento):
    tipoAccount=(
                (None, 'Selezionare tipo'),
                ('sk','Skype'),
                ('fb','Facebook'),
                ('tw','Twitter'),
                ('li','LinkedIn')
                )   
    tipo=models.CharField('Tipo Account',max_length=2,choices=tipoAccount)
    userid=models.CharField('Account',max_length=50);
     
class Telefono(Riferimento):
    tipoTel=(
           (None,'Selezionare tipo telefono'),   
           (1,'Fisso'),
           (2,'Cellulare'),
           (3,'Fax'),
     )
    tipo=models.SmallIntegerField('Tipo Telefono',choices=tipoTel)
    tipoIndirizzo=models.ForeignKey('TipoIndirizzo',blank=True,null=True)
    tipoSede=models.ForeignKey("TipoSede",related_name='tiposedeTelefono',blank=True,null=True)
    numero=models.CharField(max_length=55)
     
     
class SitoInternet(Riferimento):
    website=models.CharField('Web site',max_length=255)
     

class Indirizzo(Riferimento):
    descrizione=models.CharField('Descrizione',max_length=255,null=True,blank=True)
    ind=models.CharField('Indirizzo',max_length=255,null=True,blank=True)
    civico=models.CharField('Civico',max_length=10,null=True,blank=True)
    cap=models.CharField('Cap',max_length=5,null=True,blank=True)
    localita=models.CharField('Localita',max_length=255,null=True,blank=True)
    comune=models.ForeignKey('Comune',blank=False)
    tipo=models.ForeignKey('TipoIndirizzo')
    tipoSede=models.ForeignKey("TipoSede",related_name='tiposedeIndirizzo')
    def __str__(self):
        return self.descrizione+' '+self.ind+' '+self.civico+' '+self.cap+' '+self.localita+' '+str(self.comune)
         
