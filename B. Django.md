# Framework web
>Un framework fornisce lo scheletro, dell'applicazione. Fornisce una comoda base su cui costruire.

A differenza di una accozzaglia di libreria si trova al centro del progetto. Utilizzando le librerie è il nostro codice al centro.

Forniscono admin, page, ORD (scelta del DB diventa una configurazione rapidissima, non servono query nel codice perché autogenerato), ...

## Modello MVC
Si compone di:
- **Model** modellazione dei dati (schema dati, accesso, interpretazione, relazioni, ...). Vedi Object Relational Database.
- **View** possono esistere più viste dell'applicazione. Ad esempio mobile vs desktop.
- **Controller** interagisce tra view e modello. Esegue azioni sul modello guidato da eventi.

Il modello è "blindato", fornisce information hiding e può essere acceduto solamente mediante l'interfaccia esposta.
La vie 

Fornisce information hiding, disaccoppiamento, DRY - Don't Repeat Yourself.


#Attenzione possono cambiare ruoli e interazioni. Ad esempio il controller potrebbe essere accentrato, recuperare la vista, renderizzarla e rispondere al client HTTP.

# Modelli
## Modello MVC
Si compone di:
- **Model** modellazione dei dati (schema dati, accesso, interpretazione, relazioni, ...). Vedi Object Relational Database.
- **View** possono esistere più viste dell'applicazione. Ad esempio mobile vs desktop.
- **Controller** interagisce tra view e modello. Esegue azioni sul modello guidato da eventi.

Il modello è "blindato", fornisce information hiding e può essere acceduto solamente mediante l'interfaccia esposta.
La vie 

Fornisce information hiding, disaccoppiamento, DRY - Don't Repeat Yourself.


#Attenzione possono cambiare ruoli e interazioni. Ad esempio il controller potrebbe essere accentrato, recuperare la vista, renderizzarla e rispondere al client HTTP.

## Modello MTV
>Model Template View

# Intro di Django
>Pythonic: orientato alla prototipazione rapida, succinto, poco verboso, riusabilità, pluggability dei componenti.

#Completa

## Modello
Componenti:
- Model: models.py
- Controller: urls.py
- View: views.py

O alternativamente, modello MVT - Model View Template.

Controller suddiviso in template e view.

## Model: ORD e ORM
Il modello verrà rappresentato in Python da un **virtual object database**:
- ORD - Object Relational Database 
- ORM - Object Relational Mapping

Questo abilita all'esecuzione di query efficienti e portabili. Ci si può interfacciare al DB indipendentemente dal DBMS o linguaggio scelti.

L'interazione con il database è trasparente: SQLLite, PgSQL, ecc.

## View
In Django le viste (`view.py`) contengono anche la logica di business.
Il file `urls` contiene il mapping tra URL e vista.

## Template
>Separa la logica (view) dalla presentazione

La generazione del template è scriptata con Jinja2.
Si preferisce scrivere template in HTML al posto che in XML.

Si può alleggerire la definizione di una pagina di template, usando l'ereditarietà: `{% extends "base.html" %}` che importerà un altro template. Si definisce quindi il contenuto con `{% block content %} ... {% endblock %}`

## Tassonomia di un'applicazione
Directory hierarchy:
- mysite
	- `manage.py`
	- mysite
		- `__init__.py`
		- `settings.py`
		- `urls.py`
	- app_1
	- ...
	- app_n

`apps` are Python packages:
- `__init__.py`
- `urls.py`
- `models.py`
- `views.py`

Perché il modello si trova solo nelle sotto-app? i dati sono legati al modello.

L'URL ha una struttura gerarchica che individua il progetto principale o le sotto-app

Il file `wsgi.py` funge da gateway verso Nginx o Apache web server.

## CLI
Il modulo `manage.py <command> [options]` serve a supporto della gestione del progetto.
I comandi supportati sono:
- `startproject`
- `startapp` lancia l'applicazione che esegue sul server
- `runserver` avvia il server per lo sviluppo
- `migrate` migrazione del modello
- `dumpdata` salva dati del DB
- `loaddata` carica dati DB
- `test` unit testing