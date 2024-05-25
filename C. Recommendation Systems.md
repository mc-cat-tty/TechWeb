>CTR - Click Through Rate: rapporto tra click e impressioni.

# Introduzione
Un recommendation system è basato su un **recommendation engine**, che sfrutta un modello matematico (o una funzione obiettivo) per predirre quanto all'utente potrebbe piacere un elemento. Si possono prevedere: rating, preference, utilità, etc.

Appaiono due attori:
- utenti
- elementi da consigliare

Categorie di approcci:
- **user-based collaborative filtering**
- **content-based filtering**
- **hybrid RS**

# User-based Collaborative filtering
>Metodi basati sulla profilazione degli utenti. Analizzando grandi quantità di dati, comportamenti e attività o preferenze, si riesce a prevere cosa vorranno utenti simili.

Punti chiave:
- dato un utente, identificare quali altri utenti sono simili (preferenze, comportamento, etc). La similarità può essere calcolata con Pearson correlation coefficient e similarity, oppure relazioni tra gli utenti (eg. in social).
- identificati gli utenti simili, si consigliano elementi di cui non hanno avuto esperienza, ma che potrebbero interessargli

Non necessita conoscenza sugli elementi.
## User-Rating Matrix
>La coordinata $R_{u,i}$ identifica il rating (frequenza, preferenza, etc.) dell'utente $u$ rispetto all'elemento $i$.

Mantiene in memoria le vecchie interazioni degli utenti, per fare predizioni sull'utilizzo futuro. Lavora sotto l'assunzione che utenti che hanno interagito con articoli simili in passato continueranno a farlo in futuro.

Problema: cold start

# Content-based filtering
>Basati su descrizione degli elementi, profilo di preferenze dell'utente.

Deve estrarre un set di features dagli elementi per riuscire a calcolarne una similarità. Spesso si usa una bag of keywords. 

La similarità viene calcolata con le tecniche viste sopra sugli item, non più sugli utenti.

Problema: feature extraction

## Item-Content Matrix
>La matrice ICM è una matriche che, nella sua versione binaria, mantiene in $F_{i,f}$ il valore 1 per la feature $f$ relativa all'elemento $i$.

Ad un utente piaceranno elementi simili ai quelli che gli sono piaciuti in passato.

Possibili semplificazioni:
- calcolare similarità aggreate per utenti simili tra loro
- proporre item dall'aggregazione delle features verso cui l'utente ha mostrato interesse

# Hybrid systems
I sistemi di recommendation ibridi combinano i rank di user-based CF e content-based F.
Possono risolvere problemi come il cold-start.

# Complex Real Systems
## Tecniche
- **Matrix factorization**: decomposizione di user-rating matrix o item-content matrix per evidenziare dati latenti/pattern nascosti. Può fare predizioni su entry mancanti.
- **Deep learning**
- **Session-based recommendations**: raccomandazion in base alla sessione passata dell'utente
- **Temporal Dynamics**: suggerimenti che prendono in considerazioni la temporalità della vasita alla piattaforma (ora del giorno, giorno della settimana, etc.). Ad esempio, di notte non vorrò ordinare un cappuccino.
- **A/B Testing**: experimental testing of website by deploying two different versions of the website to two different user groups. The outcome of the experiment is determined based on predetermined objectives of KPI - Key Performance Indicator.

#Nota inserisci un recommendation system nel progetto

