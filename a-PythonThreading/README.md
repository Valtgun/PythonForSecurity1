# Write your own example using Python Threading module

Tiek izmantot requests bibliotēka:
pip3 install -r requirements.txt
vai 
pip3 install requests

Skripts izmantojot paralēlas plūsmas, katrā plūsmā veic http pieprasījumu noteiktam URL.
Paralelizējot, to var izdarīt ātrāk, saīsinot laiku.


Piemērs: python a-PythonThreading.py
1.palaišana:
```
Pieprasījuma izpildes laiks https://www.delfi.lv: 0.20 sek
Pieprasījuma izpildes laiks https://www.ss.com: 0.20 sek
Pieprasījuma izpildes laiks https://www.google.com: 0.37 sek
Pieprasījuma izpildes laiks https://www.github.com: 0.56 sek
Kopējais laiks: 0.56 sek
```

2.palaišana:
```
Pieprasījuma izpildes laiks https://www.ss.com: 0.18 sek
Pieprasījuma izpildes laiks https://www.delfi.lv: 0.19 sek
Pieprasījuma izpildes laiks https://www.google.com: 0.34 sek
Pieprasījuma izpildes laiks https://www.github.com: 0.60 sek
Kopējais laiks: 0.61 sek
```

Var redzēt, ka pieprasījumu pabeigšana ne vienmēr ir vienādā secībā, jo paralēli pieprasot kāds pieprasījums izpildās ātrāk.
Kā arī kopējais laiks ir atkarīgs no ilgākā pieprasījuma, nevis summējot katru, kas parāda, ka strādā paralēli.