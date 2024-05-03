# Introduzione
Vedi life-cycle stage vs cost of fixing a bug.
Benefici del testing: prevenire bug potenzialmente catastrofici come l'auto-distruzione del lanciatore di ESA Ariane 5.

# Categorizzazione dei test
## Granularità
Tipi di testing:
- **unit testing** - testing di unità di software minime
- **integration (acceptance) testing** - testing dell'*interazione* tra singoli componenti
- **regression testing** - verifica che le *nuove* modifiche non portino a *regressione*
- **performance (stress) testing** - valutazione livello prestazionale sotto grandi carichi

## Input
>**Black-box testing**: testing senza conoscenza degli internals del sistema in fase di testing.
- **equivalence partitioning** - derivazione di un test da ogni classe di equivalenza sull'insieme universo degli input
- **boundary value analysis** - analisi ai valori di frontiera tra le partizioni definite dall'equivalence partitioning
- **fuzz testing** - dati random e inaspettati

>**White-box testing**: testing avendo piena conoscenza degli internals del sistema:
- static testing
- code coverage

# Struttura dei test
I test sono organizzati in suite, raggruppamenti di testcases. Ogni testcase contiene più funzioni di test, ognuna volta a verificare un aspetto puntuale del modulo sotto testing.

La maggior parte dei linguaggi mette a disposizioni primitive per lo unit testing. In particolare, per l'esecuzione di una intera test suite, per il raccoglimento di report, funzioni di asserzione, ecc.

# unittest
`unittest` è il modulo offerto da Python per lo unit testing.

## Assertions
Tra le assert degne di nota sono presenti:
- `assertRaises(exception, callable, args)`: fallisce se non vengono sollevate eccezioni; ritorna errore se l'eccezione è diversa da quella attesa (la propaga)
- `assert[AlmostEqual|AlmostNotEqual](a, b, msg, places=7, delta=None)`: verifica che due valori siano uguali (o diversi) entro le 7 (o qualsivoglia valore di precisione) cifre decimali, oppure entro un certo scarto
- `assert[Equal|NotEqual](a, b, msg)`
- `assert[True|False](expr, msg)`
- `assert[Greater|GraterEqual](a, b)`
- `assert[Less|LessEqual](a, b)`
- `assert[RegexpMatches|NotRegexpMatches](text, regex)`

## Esiti
- OK - esito positivo
- FAIL - esito negativo (assertion fallita)
- ERROR - errore di altra natura, diverso da `AssertionError`

