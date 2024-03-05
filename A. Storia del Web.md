# Intro: Internet vs Web
Internet nasce nel '69 dalla rete ARPANET. Contesto: guerra fredda, dopo che l'URRS raggiunge lo spazio. Ridondanza riflette il timore di un attacco nucleare Russo dallo spazio. Finanziato dal ministero della difesa americano.

Il web nasce nell'89 dall'esigenza di Tim Barners Lee di condividere paper mentre lavorava al CERN. Sulla base di TCP/IP si sviluppa HTTP, HTML e DNS (URL ASCII identificativo della pagina).

#Vedi HyperCard e HyperTalk

>Il web è un servizio, la rete lo supporta.

Le pagine erano inizialmente statiche, ma navigabili (idea di ipertesto/ancora)

Web 2.0 nel 2004:
- web as a platform
- from web readonly to web read and write
- la banda, da asimmetrica, inizia a dare importanza anche all'upload

Web 3.0:
- semantic web
- cookies di terze parti
- RDF

Cookie di "prima parte": pezzi di informazione lasciati da un server per riconoscere il client quando torna.
Cookie di "terze parti": cookie lasciati dai fornitori di pubblicità (eg: banner)

# Web dinamico
>Applicazioni web che restituiscono pagine tailor-made sulla base di informazioni ricevute dagli utenti.

Il primo strumento è la **Common Gateway Interface - CGI -**. Il server HTTP, ricevuta una richiesta di pagina web, invoca il programma CGI, che si occupa dell'interazione con il DB e costruisce la pagina di risposta.

Lo standard di comunicazione con il server dipende; tipicamente l'interazione avviene per mezzo di stdin/stdout.

Problemi:
- scalabilità
- mancanza di modularità (SQL in script, con info e struttura pagina)
- scarsa manutenibilità

Nascono **fast CGI** che permettono di lanciare un'istanza condivisa tra più utenze.
- **Server API**
- **Moduli di Apache Server** (mod_php, mod_python, ...), che permettono di interpretare gli script direttamente dal processo del server.
- **Active Server Pages**: 
- **Java Servlets**
- **PHP** linguaggio dell'anno nel 2004
- Verso i web framework: ASP.NET, Ruby on rails, Django

#Vedi Laravel

## Framework web
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
