from django.http import HttpResponse

import csv
from GestioneRiferimenti.models import Email,Indirizzo,Telefono
from GestionePersone.models import Persona
from GestioneSoggetti.models import Ente,Soggetto,Adesione
from GestioneIncarichi.models import IncaricoIstituzionale
from django.utils.encoding import smart_str



def getEmail():
    rif=Email.objects.all().values(#1
                                   'soggetto__id',\
                                   'soggetto__denominazione',\
                                   'soggetto__tiposoggetto__descr',\
                                   'soggetto__tipo',\
                                   'soggetto__dettaglio',\
                                   'soggetto__provenienza',
                                   'soggetto__cf',\
                                   'soggetto__pi',\
                                   'soggetto__provincia__descrizione',\
                                   'soggetto__regione__descrizione',\
                                   'soggetto__ente__tipoContatto__descr',\
                                   'soggetto__ente__tipoEnte__descr',\
                                   'soggetto__ente__orienPolitico__descr',\
                                   'soggetto__ente__annoIniLegisl',\
                                   'soggetto__note',\
                                   #2
                                   'persona__id','persona__cognome','persona__nome',\
                                   'persona__cf','persona__dataNascita','persona__luogocomune__descrizione',\
                                   'persona__lavoratoap','persona__note',\
                                   'persona__provincia__descrizione',\
                                   'persona__regione__descrizione',\
                                   'persona__strutturaSoggetto__soggetto__id',\
                                   'persona__strutturaSoggetto__soggetto__denominazione',\
                                   'persona__strutturaSoggetto__soggetto__tiposoggetto__descr',\
                                   'persona__strutturaSoggetto__soggetto__tipo',\
                                   'persona__strutturaSoggetto__soggetto__dettaglio',\
                                   'persona__strutturaSoggetto__soggetto__provenienza',\
                                   'persona__strutturaSoggetto__soggetto__cf',\
                                   'persona__strutturaSoggetto__soggetto__pi',\
                                   'persona__strutturaSoggetto__soggetto__provincia__descrizione',\
                                   'persona__strutturaSoggetto__soggetto__regione__descrizione',\
                                   'persona__strutturaSoggetto__soggetto__ente__tipoContatto__descr',\
                                   'persona__strutturaSoggetto__soggetto__ente__tipoEnte__descr',\
                                   'persona__strutturaSoggetto__soggetto__ente__orienPolitico__descr',\
                                   'persona__strutturaSoggetto__soggetto__ente__annoIniLegisl',\
                                   'persona__strutturaSoggetto__soggetto__note',\
                                   'persona__strutturaSoggetto__struttura__organo',\
                                   'persona__strutturaSoggetto__struttura__ruolo',\
                                   'persona__strutturaSoggetto__delega__descr',\
                                   'persona__strutturaSoggetto__rappleg',\
                                   'persona__incaricoistituzionale__refpol',\
                                   'persona__incaricoistituzionale__reftec',\
                                   #4
                                   'incaricoIst__strutturasoggetto__soggetto__id',\
                                   'incaricoIst__strutturasoggetto__soggetto__denominazione',\
                                   'incaricoIst__strutturasoggetto__soggetto__tiposoggetto__descr',\
                                   'incaricoIst__strutturasoggetto__soggetto__tipo',\
                                   'incaricoIst__strutturasoggetto__soggetto__dettaglio',\
                                   'incaricoIst__strutturasoggetto__soggetto__provenienza',\
                                   'incaricoIst__strutturasoggetto__soggetto__cf',\
                                   'incaricoIst__strutturasoggetto__soggetto__pi',\
                                   'incaricoIst__strutturasoggetto__soggetto__provincia__descrizione',\
                                   'incaricoIst__strutturasoggetto__soggetto__regione__descrizione',\
                                   'incaricoIst__strutturasoggetto__soggetto__ente__tipoContatto__descr',\
                                   'incaricoIst__strutturasoggetto__soggetto__ente__tipoEnte__descr',\
                                   'incaricoIst__strutturasoggetto__soggetto__ente__orienPolitico__descr',\
                                   'incaricoIst__strutturasoggetto__soggetto__ente__annoIniLegisl',\
                                   'incaricoIst__strutturasoggetto__soggetto__note',\
                                   'incaricoIst__strutturasoggetto__struttura__organo',\
                                   'incaricoIst__strutturasoggetto__struttura__ruolo',\
                                   'incaricoIst__strutturasoggetto__delega__descr',\
                                   'incaricoIst__strutturasoggetto__rappleg',\
                                   'incaricoIst__persona__id',\
                                   'incaricoIst__persona__cognome',\
                                   'incaricoIst__persona__nome',\
                                   'incaricoIst__persona__cf',\
                                   'incaricoIst__persona__dataNascita',\
                                   'incaricoIst__persona__luogocomune__descrizione',\
                                   'incaricoIst__persona__lavoratoap',\
                                   'incaricoIst__persona__note',\
                                   'incaricoIst__persona__provincia__descrizione',\
                                   'incaricoIst__persona__regione__descrizione',\
                                   'incaricoIst__refpol',\
                                   'incaricoIst__reftec',\
                                   #5
                                   'strutturaSoggetto__soggetto__id',\
                                   'strutturaSoggetto__soggetto__denominazione',\
                                   'strutturaSoggetto__soggetto__tiposoggetto__descr',\
                                   'strutturaSoggetto__soggetto__tipo',\
                                   'strutturaSoggetto__soggetto__dettaglio',\
                                   'strutturaSoggetto__soggetto__provenienza',\
                                   'strutturaSoggetto__soggetto__cf',\
                                   'strutturaSoggetto__soggetto__pi',\
                                   'strutturaSoggetto__soggetto__provincia__descrizione',\
                                   'strutturaSoggetto__soggetto__regione__descrizione',\
                                   'strutturaSoggetto__soggetto__ente__tipoContatto__descr',\
                                   'strutturaSoggetto__soggetto__ente__tipoEnte__descr',\
                                   'strutturaSoggetto__soggetto__ente__orienPolitico__descr',\
                                   'strutturaSoggetto__soggetto__ente__annoIniLegisl',\
                                   'strutturaSoggetto__soggetto__note',\
                                   'strutturaSoggetto__persona__id',
                                   'strutturaSoggetto__persona__cognome',\
                                   'strutturaSoggetto__persona__nome',\
                                   'strutturaSoggetto__persona__cf',\
                                   'strutturaSoggetto__persona__dataNascita',\
                                   'strutturaSoggetto__persona__luogocomune__descrizione',\
                                   'strutturaSoggetto__persona__lavoratoap',\
                                   'strutturaSoggetto__persona__note',\
                                   'strutturaSoggetto__persona__provincia__descrizione',\
                                   'strutturaSoggetto__persona__regione__descrizione',\
                                   'strutturaSoggetto__struttura__organo',\
                                   'strutturaSoggetto__struttura__ruolo',\
                                   'strutturaSoggetto__delega__descr',\
                                   'strutturaSoggetto__rappleg',\
                                   'strutturaSoggetto__incaricoistituzionale__refpol',\
                                   'strutturaSoggetto__incaricoistituzionale__reftec',\
                                   'tipo',\
                                   'tipoSede__descr',\
                                   'address')
    for row in rif:
        row['soggetto_id']=row.get('soggetto__id')
        row['soggetto']=row.get('soggetto__denominazione')
        row['tiposoggetto']=row.get('soggetto__tiposoggetto__descr')
        row['descrizione']=row.get('soggetto__tipo')
        row['specifica']=row.get('soggetto__dettaglio')
        row['sede']=row.get('soggetto__provenienza')
        row['cf']=row.get('soggetto__cf')
        row['pi']=row.get('soggetto__pi')
        row['soggprov']=row.get('soggetto__provincia__descrizione')
        row['soggreg']=row.get('soggetto__regione__descrizione')
        row['pi']=row.get('soggetto__pi')
        row['soggettoNota']=row.get('soggetto__note')

        row['tipoContatto']=row.get('soggetto__ente__tipoContatto__descr')
        row['tipoEnte']=row.get('soggetto__ente__tipoEnte__descr')
        row['orienPolitico']=row.get('soggetto__ente__orienPolitico__descr')
        row['annoIniLegisl']=row.get('soggetto__ente__annoIniLegisl')

        row['persona_id']=row.get('persona__id')        
        row['cognome']=row.get('persona__cognome')
        row['nome']=row.get('persona__nome')
        
        row['personacf']=row.get('persona__cf')
        row['personaNascita']='' if row.get('persona__dataNascita')==None else row.get('persona__dataNascita').strftime('%d/%m/%Y')
        row['personaNascitaComune']=row.get('persona__luogocomune__descrizione')
        row['personaTipo']='' if row['persona_id']==None else '|'.join(s.descr for s in Persona.objects.get(id=row.get('persona__id')).tipo.all())
        row['personaCompetenza']='' if row['persona_id']==None else '|'.join(s.descr for s in Persona.objects.get(id=row.get('persona__id')).competenza.all())
        row['personaLavoratoap']=row.get('persona__lavoratoap')
        row['personaNota']=row.get('persona__note')
        row['personaprov']=row.get('persona__provincia__descrizione')
        row['personareg']=row.get('persona__regione__descrizione')
                     
        row['IncIst_soggetto_id']=row.get('incaricoIst__strutturasoggetto__soggetto__id')
        row['IncIst_tiposoggetto']=row.get('incaricoIst__strutturasoggetto__soggetto__tiposoggetto__descr')
        row['IncIst_soggetto']=row.get('incaricoIst__strutturasoggetto__soggetto__denominazione')
        row['IncIst_descrizione']=row.get('incaricoIst__strutturasoggetto__soggetto__tipo')
        row['IncIst_specifica']=row.get('incaricoIst__strutturasoggetto__soggetto__dettaglio')
        row['IncIst_sede']=row.get('incaricoIst__strutturasoggetto__soggetto__provenienza')
        row['IncIst_cf']=row.get('incaricoIst__strutturasoggetto__soggetto__cf')
        row['IncIst_pi']=row.get('incaricoIst__strutturasoggetto__soggetto__pi')
        row['IncIst_soggprov']=row.get('incaricoIst__strutturasoggetto__soggetto__provincia__descrizione')
        row['IncIst_soggreg']=row.get('incaricoIst__strutturasoggetto__soggetto__regione__descrizione')
        
        row['IncIst_tipoContatto']=row.get('incaricoIst__strutturasoggetto__soggetto__ente__tipoContatto__descr')
        row['IncIst_tipoEnte']=row.get('incaricoIst__strutturasoggetto__soggetto__ente__tipoEnte__descr')
        row['IncIst_orienPolitico']=row.get('incaricoIst__strutturasoggetto__soggetto__ente__orienPolitico__descr')
        row['IncIst_annoIniLegisl']=row.get('incaricoIst__strutturasoggetto__soggetto__ente__annoIniLegisl')
        row['IncIst_soggettoNota']=row.get('incaricoIst__strutturasoggetto__soggetto__note')
        row['IncIst_organo']=row.get('incaricoIst__strutturasoggetto__struttura__organo')
        row['IncIst_ruolo']=row.get('incaricoIst__strutturasoggetto__struttura__ruolo')
        row['IncIst_delega']=row.get('incaricoIst__strutturasoggetto__delega__descr')
        row['IncIst_rappleg']=row.get('incaricoIst__strutturasoggetto__rappleg')
        
        
                     
        row['IncIst_persona_id']=row.get('incaricoIst__persona__id')
        row['IncIst_cognome']=row.get('incaricoIst__persona__cognome')
        row['IncIst_nome']=row.get('incaricoIst__persona__nome')
        row['IncIst_cf']=row.get('incaricoIst__persona__cf')
        row['IncIst_dataNascita']='' if row.get('incaricoIst__persona__dataNascita')==None else row.get('incaricoIst__persona__dataNascita').strftime('%d/%m/%Y')
        row['IncIst_Nascitacomune']=row.get('incaricoIst__persona__luogocomune__descrizione')
        row['IncIst_lavoratoap']=row.get('incaricoIst__persona__lavoratoap')
        row['IncIst_Personanote']=row.get('incaricoIst__persona__note')
        row['IncIst_personaTipo']='' if row['IncIst_persona_id']==None else '|'.join(s.descr for s in Persona.objects.get(id=row.get('IncIst_persona_id')).tipo.all())
        row['IncIst_personaCompetenza']='' if row['IncIst_persona_id']==None else '|'.join(s.descr for s in Persona.objects.get(id=row.get('IncIst_persona_id')).competenza.all())
        row['IncIst_personaNota']=row.get('incaricoIst__persona__note')
        row['IncIst_personaprov']=row.get('incaricoIst__persona__provincia__descrizione')
        row['IncIst_personareg']=row.get('incaricoIst__persona__regione__descrizione')
        row['IncIst_refpol']=row.get('incaricoIst__refpol')
        row['IncIst_reftec']=row.get('incaricoIst__reftec')
        
        row['StruSogg_soggetto_id']=row.get('strutturaSoggetto__soggetto__id')
        row['StruSogg_soggetto']=row.get('strutturaSoggetto__soggetto__denominazione')
        row['StruSogg_tiposoggetto']=row.get('strutturaSoggetto__soggetto__tiposoggetto__descr')
        row['StruSogg_descrizione']=row.get('strutturaSoggetto__soggetto__tipo')
        row['StruSogg_specifica']=row.get('strutturaSoggetto__soggetto__dettaglio')
        row['StruSogg_sede']=row.get('strutturaSoggetto__soggetto__provenienza')
        row['StruSogg_cf']=row.get('strutturaSoggetto__soggetto__cf')
        row['StruSogg_pi']=row.get('strutturaSoggetto__soggetto__pi')
        row['StruSogg_soggprov']=row.get('strutturaSoggetto__soggetto__provincia__descrizione')
        row['StruSogg_soggreg']=row.get('strutturaSoggetto__soggetto__regione__descrizione')
        
        row['StruSogg_tipoContatto']=row.get('strutturaSoggetto__soggetto__ente__tipoContatto__descr')
        row['StruSogg_tipoEnte']=row.get('strutturaSoggetto__soggetto__ente__tipoEnte__descr')
        row['StruSogg_orienPolitico']=row.get('strutturaSoggetto__soggetto__ente__orienPolitico__descr')
        row['StruSogg_annoIniLegisl']=row.get('strutturaSoggetto__soggetto__ente__annoIniLegisl')
        row['StruSogg_soggettoNota']=row.get('strutturaSoggetto__soggetto__note')
             
        row['StruSogg_persona_id']=row.get('strutturaSoggetto__persona__id')
        row['StruSogg_cognome']=row.get('strutturaSoggetto__persona__cognome')
        row['StruSogg_nome']=row.get('strutturaSoggetto__persona__nome')
        row['StruSogg_cf']=row.get('strutturaSoggetto__persona__cf')
        row['StruSogg_dataNascita']='' if row.get('strutturaSoggetto__persona__dataNascita')==None else row.get('strutturaSoggetto__persona__dataNascita').strftime('%d/%m/%Y')
        row['StruSogg_datanascitaComune']=row.get('strutturaSoggetto__persona__luogocomune__descrizione')
        row['StruSogg_lavoratoap']=row.get('strutturaSoggetto__persona__lavoratoap')
        row['StruSogg_Personanota']=row.get('strutturaSoggetto__persona__note')
        row['StruSogg_personaprov']=row.get('strutturaSoggetto__persona__provincia__descrizione')
        row['StruSogg_personareg']=row.get('strutturaSoggetto__persona__regione__descrizione')

        row['StruSogg_refpol']=row.get('strutturaSoggetto__incaricoistituzionale__refpol')
        row['StruSogg_reftec']=row.get('strutturaSoggetto__incaricoistituzionale__reftec')
        row['StruSogg_personaTipo']='' if row['StruSogg_persona_id']==None else '|'.join(s.descr for s in Persona.objects.get(id=row.get('StruSogg_persona_id')).tipo.all())
        row['StruSogg_personaCompetenza']='' if row['StruSogg_persona_id']==None else '|'.join(s.descr for s in Persona.objects.get(id=row.get('StruSogg_persona_id')).competenza.all())
       
        row['StruSogg_rappleg']=row.get('strutturaSoggetto__rappleg')
        row['StruSogg_organo']=row.get('strutturaSoggetto__struttura__organo')
        row['StruSogg_ruolo']=row.get('strutturaSoggetto__struttura__ruolo')
        row['StruSogg_delega']=row.get('strutturaSoggetto__delega__descr')
        

        row['PersIncStrutt_soggetto']=row.get('persona__strutturaSoggetto__soggetto__denominazione')
        
        #---------------------------------------------------------------------------
        row['PersIncStrutt_soggetto_id']=row.get('persona__strutturaSoggetto__soggetto__id')
        row['PersIncStrutt_soggetto']=row.get('persona__strutturaSoggetto__soggetto__denominazione')
        row['PersIncStrutt_tiposoggetto']=row.get('persona__strutturaSoggetto__soggetto__tiposoggetto__descr')
        row['PersIncStrutt_descrizione']=row.get('persona__strutturaSoggetto__soggetto__tipo')
        row['PersIncStrutt_specifica']=row.get('persona__strutturaSoggetto__soggetto__dettaglio')
        row['PersIncStrutt_sede']=row.get('persona__strutturaSoggetto__soggetto__provenienza')
        row['PersIncStrutt_cf']=row.get('persona__strutturaSoggetto__soggetto__cf')
        row['PersIncStrutt_pi']=row.get('persona__strutturaSoggetto__soggetto__pi')
        row['PersIncStrutt_soggprov']=row.get('persona__strutturaSoggetto__soggetto__provincia__descrizione')
        row['PersIncStrutt_soggreg']=row.get('persona__strutturaSoggetto__soggetto__regione__descrizione')
        row['PersIncStrutt_tipoContatto']=row.get('persona__strutturaSoggetto__soggetto__ente__tipoContatto__descr')
        row['PersIncStrutt_tipoEnte']=row.get('persona__strutturaSoggetto__soggetto__ente__tipoEnte__descr')
        row['PersIncStrutt_orienPolitico']=row.get('persona__strutturaSoggetto__soggetto__ente__orienPolitico__descr')
        row['PersIncStrutt_annoIniLegisl']=row.get('persona__strutturaSoggetto__soggetto__ente__annoIniLegisl')
        row['PersIncStrutt_soggettoNota']=row.get('persona__strutturaSoggetto__soggetto__note')
        row['PersIncStrutt_organo']=row.get('persona__strutturaSoggetto__struttura__organo')
        row['PersIncStrutt_ruolo']=row.get('persona__strutturaSoggetto__struttura__ruolo')
        row['PersIncStrutt_delega']=row.get('persona__strutturaSoggetto__delega__descr')
        row['PersIncStrutt_rappleg']=row.get('persona__strutturaSoggetto__rappleg')
        row['PersIncStrutt_refpol']=row.get('persona__incaricoistituzionale__refpol')
        row['PersIncStrutt_reftec']=row.get('persona__incaricoistituzionale__reftec')
          
#------------------------------------------
        

        row['emailtipo']=row.get('tipo')
        row['emailtipoSede']=row.get('tipoSede__descr')
        row['email']=row.get('address')
        
    return rif
def export_email(request):
    response = HttpResponse(content_type='text/csv')#
    response['Content-Disposition'] = 'attachment; filename=gestionale_email.csv'
 
    lrif=list(getEmail())
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['codiceSoggetto','codicePersona','Soggetto','Descrizione','Specifica','Sede','cf','pi','Soggetto_provincia','Soggetto_regione',\
                     'TipoSoggetto','TipoContatto','TipoEnte','Socio','OrientamentoPolitico','AnnoInizioLegisl', 'SoggettoNota',\
                     'Cognome','Nome','CF','Data Nascita','Comune Nascita','Tipo','Competenza','LavoratoAP','Nota','Persona_provincia','Persona_regione',\
                     'Organo','Ruolo','Delega','OrganoRuolo AP','RerefentePolitico','ReferenteTecnico',\
                     'RapprLegale','tipoEmail','tipoSede','email'])
    ap=Soggetto.objects.filter(denominazione__icontains='avviso pubblico')
    for rowi in lrif:
        
        codiceSoggetto=rowi.get('IncIst_soggetto_id') or rowi.get('StruSogg_soggetto_id') or rowi.get('soggetto_id')  or rowi.get('PersIncStrutt_soggetto_id') or ''
        codicePersona=rowi.get('persona_id')  or rowi.get('IncIst_persona_id') or rowi.get('StruSogg_persona_id') or '' 
        
        soggetto=rowi.get('IncIst_soggetto') or rowi.get('StruSogg_soggetto') or rowi.get('soggetto') or rowi.get('PersIncStrutt_soggetto') or ''
        descrizione=rowi.get('descrizione') or rowi.get("StruSogg_descrizione") or rowi.get("IncIst_descrizione") or rowi.get('PersIncStrutt_descrizione') or ''
        specifica=rowi.get('specifica') or rowi.get("StruSogg_specifica") or rowi.get("IncIst_specifica") or rowi.get('PersIncStrutt_specifica') or ''
        sede=rowi.get('sede') or rowi.get("StruSogg_sede") or rowi.get("IncIst_sede") or rowi.get('PersIncStrutt_sede') or ''
        cf=rowi.get('cf') or rowi.get("StruSogg_cf") or rowi.get("IncIst_cf") or rowi.get('PersIncStrutt_cf') or ''
        pi=rowi.get('pi') or rowi.get("StruSogg_pi") or rowi.get("IncIst_pi") or rowi.get('PersIncStrutt_pi') or ''
        soggetto_prov=rowi.get('soggprov') or rowi.get("StruSogg_soggprov") or rowi.get("IncIst_soggprov") or rowi.get('PersIncStrutt_soggprov') or ''
        soggetto_reg=rowi.get('soggreg') or rowi.get("StruSogg_soggreg") or rowi.get("IncIst_soggreg") or rowi.get('PersIncStrutt_soggreg') or ''
        tiposoggetto=rowi.get('tiposoggetto') or rowi.get("StruSogg_tiposoggetto") or rowi.get("IncIst_tiposoggetto") or rowi.get('PersIncStrutt_tiposoggetto') or ''
        tipocontatto=rowi.get('tipoContatto') or rowi.get('IncIst_tipoContatto') or rowi.get('StruSogg_tipoContatto') or rowi.get('PersIncStrutt_tipoContatto') or '' 
        tipoente=rowi.get('tipoEnte') or rowi.get('IncIst_tipoEnte') or  rowi.get('StruSogg_tipoEnte') or rowi.get('PersIncStrutt_tipoEnte') or ''
        socio='' if (codiceSoggetto=='' or codiceSoggetto==None) else \
            ('SI' if Ente.objects.get(soggetto_ptr_id=codiceSoggetto).isSocio()  else  'NO' ) if tiposoggetto=='Ente' else ''

        orientpol=rowi.get('orienPolitico') or rowi.get('IncIst_orienPolitico') or rowi.get('StruSogg_orienPolitico') or rowi.get('PersIncStrutt_orienPolitico') or ''
        annoIleg=rowi.get('annoIniLegisl') or rowi.get('IncIst_annoIniLegisl') or rowi.get('StruSogg_annoIniLegisl') or rowi.get('PersIncStrutt_annoIniLegisl') or ''
        soggettoNota=(rowi.get('soggettoNota') or rowi.get('IncIst_soggettoNota') or rowi.get('StruSogg_soggettoNota') or
                      rowi.get('PersIncStrutt_soggettoNota') or '').replace("\r\n"," ").replace(",","").replace(";","")
        
        
        cognome= rowi.get('cognome') or rowi.get('IncIst_cognome') or rowi.get('StruSogg_cognome') or ''  
        nome= rowi.get('nome') or  rowi.get('IncIst_nome') or rowi.get('StruSogg_nome') or ''  
        personacf=rowi.get('personacf') or rowi.get('IncIst_cf') or rowi.get('StruSogg_cf') or ''  
        personaNascita=rowi.get('personaNascita') or rowi.get('IncIst_dataNascita') or rowi.get('StruSogg_dataNascita') or ''  
        personaNascitaComune=rowi.get('personaNascitaComune') or rowi.get('IncIst_Nascitacomune') or rowi.get('StruSogg_datanascitaComune') or ''
        personaTipo=rowi.get('personaTipo') or '' or  rowi.get('IncIst_personaTipo') or rowi.get('StruSogg_personaTipo')  
        personaCompetenza=rowi.get('personaCompetenza') or '' or rowi.get('IncIst_personaCompetenza') or rowi.get('StruSogg_personaCompetenza')  
        personaLavoratoap=rowi.get('personaLavoratoap') or rowi.get('IncIst_lavoratoap') or rowi.get('StruSogg_lavoratoap') or ''   
        personaNota=(rowi.get('personaNota')  or rowi.get('IncIst_Personanote') or rowi.get('StruSogg_Personanota') or '').replace("\r\n"," ")
        personaprov=rowi.get('personaprov')  or rowi.get('IncIst_personaprov') or rowi.get('StruSogg_personaprov') or '' 
        personareg=rowi.get('personareg')  or rowi.get('IncIst_personareg') or rowi.get('StruSogg_personareg') or ''
        organo= rowi.get('IncIst_organo') or rowi.get('StruSogg_organo') or rowi.get('PersIncStrutt_organo') or ''
        ruolo=  rowi.get('IncIst_ruolo') or rowi.get('StruSogg_ruolo') or rowi.get('PersIncStrutt_ruolo') or ''
        orap=''
        if codicePersona!='':
            persona=Persona.objects.filter(id=codicePersona)
            aporganoruolo=persona.filter(strutturaSoggetto__soggetto=ap).values_list('strutturaSoggetto__struttura__organo','strutturaSoggetto__struttura__ruolo')
            if aporganoruolo.count()==1:
                orap=aporganoruolo[0][0]+' - '+aporganoruolo[0][1]
            else:
                orap='|'.join((s[0]+' - '+s[1]) for s in aporganoruolo)    
        organoruolo_ap=orap
        delega= rowi.get('StruSogg_delega') or rowi.get('IncIst_delega') or rowi.get('PersIncStrutt_delega') or ''
        rapplegu=rowi.get('StruSogg_rappleg') or rowi.get('IncIst_rappleg') or rowi.get('PersIncStrutt_rappleg') or ''
        refpolu=rowi.get('IncIst_refpol') or rowi.get('PersIncStrutt_refpol') or rowi.get('StruSogg_refpol') or ''
        reftecu=rowi.get('IncIst_reftec') or rowi.get('PersIncStrutt_reftec') or rowi.get('StruSogg_reftec') or ''
        refpol='SI' if refpolu==1 else 'NO'  
        reftec='SI' if reftecu==1 else 'NO'
        rappleg='SI' if rapplegu==1 else 'NO' 

        row=[smart_str(codiceSoggetto) \
            ,smart_str(codicePersona) \
            ,smart_str(soggetto) \
            ,smart_str(descrizione) \
            ,smart_str(specifica)\
            ,smart_str(sede)\
            ,smart_str(cf)\
            ,smart_str(pi)\
            ,smart_str(soggetto_prov)\
            ,smart_str(soggetto_reg)\
            ,smart_str(tiposoggetto)\
            ,smart_str(tipocontatto)\
            ,smart_str(tipoente)\
            ,smart_str(socio)\
            ,smart_str(orientpol)\
            ,smart_str(annoIleg)\
            ,smart_str(soggettoNota)\
            ,smart_str(cognome) \
            ,smart_str(nome) \
            ,smart_str(personacf) \
            ,smart_str(personaNascita) \
            ,smart_str(personaNascitaComune) \
            ,smart_str(personaTipo) \
            ,smart_str(personaCompetenza) \
            ,smart_str(personaLavoratoap) \
            ,smart_str(personaNota) \
            ,smart_str(personaprov) \
            ,smart_str(personareg) \
            ,smart_str(organo) \
            ,smart_str(ruolo) \
            ,smart_str(delega) \
            ,smart_str(organoruolo_ap) \
            ,smart_str(refpol) \
            ,smart_str(reftec) \
            ,smart_str(rappleg) \
            ,smart_str(rowi.get('emailtipo')) \
            ,smart_str(rowi.get('emailtipoSede')) \
            ,smart_str(rowi.get('email')) \
             ]
        

        writer.writerow(row)
              
    
    return response

