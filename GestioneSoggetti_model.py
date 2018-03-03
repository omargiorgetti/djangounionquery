from django.db import models

from django.utils import timezone



class TipoSoggetto (models.Model):
    descr=models.CharField('Tipo',max_length=255)
    isEnte=models.SmallIntegerField()
    
    def __str__(self):
        return self.descr 

class Soggetto(models.Model):
    tiposoggetto=models.ForeignKey('TipoSoggetto',blank=False)
    tipo=models.CharField('Descrizione',max_length=255,null=False,blank=False)
    denominazione=models.CharField('Denominazione',max_length=50,null=False,blank=False)
    dettaglio=models.CharField('Specifica',max_length=50,null=True,blank=True)
    provenienza=models.CharField('Sede',max_length=255,null=True,blank=True)
    cf=models.CharField('Codice Fiscale',max_length=16,null=True,blank=True)
    pi=models.CharField('Partita Iva',max_length=11,null=True,blank=True)
    note=models.TextField('Nota',max_length=1000,null=True,blank=True)
    struttura=models.ManyToManyField('GestioneIncarichi.Struttura',through='GestioneIncarichi.StrutturaSoggetto')
    provincia=models.ForeignKey('GestioneRiferimenti.Provincia',null=True,blank=True)
    regione=models.ForeignKey('GestioneRiferimenti.Regione',null=True,blank=True)
    

    def __unicode__(self):
        return self.denominazione+' ('+self.tiposoggetto.descr+')'     
    
    #Non Abstract perche' abbiamo la possibilita' di fare query su soggetto
    #indiependentemente dal tipo

class Stato(models.Model):
    descr=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    
    def __unicode__(self):
        return '%s - %s' % (self.tipo,self.descr) 
    
class TipoEnte (models.Model):
    descr=models.CharField(max_length=50)
    livello=models.SmallIntegerField('Livello') #livello 1 e' il base livello 2 e' se vi appartengno livelli 1 
    compostoda=models.SmallIntegerField('Composto da')
    
    def __unicode__(self):
        return self.descr

class TipoContatto (models.Model):
    descr=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.descr    

class OrienPolitico (models.Model):
    descr=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.descr    
class TipoDelibera(models.Model):
    descr=models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.descr


class pagamento(models.Model):
    descr = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descr


class Ente(Soggetto):
    codice=models.CharField('Codice',max_length=10,null=True,blank=True)
    dataAgg=models.DateTimeField('Data Aggiornamento',default=timezone.now)
    tipoEnte=models.ForeignKey('TipoEnte',null=False,blank=False)
    tipoContatto=models.ForeignKey('TipoContatto',null=True,blank=True)
    orienPolitico=models.ForeignKey('OrienPolitico',null=True,blank=True)
    annoIniLegisl=models.PositiveSmallIntegerField('Anno inizio Legislatura',null=True,blank=True)
    entePadre=models.ForeignKey('self',null=True,blank=True,default=None,related_name='AppartieneAEnte')
    statoEnte=models.ManyToManyField(Stato,through='StatoEnte')
    pagamento=models.ForeignKey('pagamento',null=True,blank=True)
            
    def __unicode__(self):
        return "%s - %s - %s" % (self.denominazione,self.tiposoggetto.descr,self.tipoEnte.descr)
    def isSocio(self):
        return StatoEnte.objects.filter(ente_id=self.id).filter(datafin=None).values_list('stato_id',flat=True)[0]==20
     
    def get_tipoEnte_descr(self):
        return self.tipoEnte.descr
class StatoEnte(models.Model):
    ente = models.ForeignKey(Ente,related_name='ente_stati')
    stato = models.ForeignKey(Stato)
    dataContatto=models.DateField('Data contatto',null=True,blank=True)
    dataAdesione=models.DateField('Data adesione',null=True,blank=True)
    dataRecesso=models.DateField('Data recesso',null=True,blank=True)
    dataDecadEsclus=models.DateField('Data decadenza/esclusione',null=True,blank=True)
    note=models.TextField('Nota',null=True,blank=True)
    dataAgg=models.DateTimeField(null=False,blank=True)
    dataini=models.DateField(null=False,blank=True)
    datafin=models.DateField(null=True,blank=True)

    def __unicode__(self): 
        if self.stato_id==0:
            return '%s - %s ' % (self.stato.tipo,self.stato.descr)
        elif self.stato_id==10:
            return "%s - %s - data contatto %s" %  (self.stato.tipo,self.stato.descr,self.dataContatto.strftime('%d/%m/%Y'))
        elif self.stato_id==20:
            return "%s - %s - data adesione il %s" %  (self.stato.tipo,self.stato.descr,self.dataAdesione.strftime('%d/%m/%Y'))
        elif self.stato_id==30:
            return "%s - %s - data decadenza/esclusione il %s" %  (self.stato.tipo,self.stato.descr,self.dataDecadEsclus.strftime('%d/%m/%Y'))
        elif self.stato_id==50:
            return "%s - %s - data recesso il %s" %  (self.stato.tipo,self.stato.descr,self.dataRecesso.strftime('%d/%m/%Y'))
        else:
            return "all"
    
class Adesione (models.Model):
    tipoDelibera=models.ForeignKey(TipoDelibera)
    dataDelibera=models.DateField('Data Delibera')
    dataAccettUffPres=models.DateField('Data accettazione Ufficio Presidenza')
    numero=models.CharField('Numero',max_length=50,null=True,blank=True)
    quota=models.DecimalField(max_digits=10, decimal_places=2)
    statoente=models.OneToOneField(StatoEnte,limit_choices_to={'stato':20})
    note=models.TextField('Nota',blank=True,null=True)
    
    def __unicode__(self):
        if not self:
            return ''
        else:    
            return "%s N.%s del %s - Quota: %d"%(self.tipoDelibera.descr,self.numero,self.dataDelibera.strftime('%d/%m/%Y'),self.quota)
            

