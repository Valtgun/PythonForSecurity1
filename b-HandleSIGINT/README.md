# Make use of Python signal handlers to handle SIGINT

Signal bibliotēka pārtver SIGINT (Ctrl+C) un iziet no cikla
10 sekundēs uzdevums pabeigsies, bet var pārtraukt izmantojot CTRL+C un tad izpildīs funkciju handle_signal()

Piemērs: python b-HandleSIGINT.py
1.palaišana: sagaida 10 sekundes
```
Sākt apstrādi. CTRL+C lai izietu
100% pabeigts...
Nepaspēji nospiest Ctrl+C.
```

2.palaišana: nospiež CTRL+C
```
Sākt apstrādi. CTRL+C lai izietu
10% pabeigts...
Graceful - pareiza skripta pabeigšana.
```

Tests, ja nokomentēta 11.rinda, un nospiež CTRL+C
```
Sākt apstrādi. CTRL+C lai izietu
20% pabeigts...
Pārtraukts, izgāja nekorekti!
```
