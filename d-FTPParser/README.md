# Create FTP site parser

FTP linki paņemti no http://www.diam.unige.it/informatica/documentazione/httpd_docs/ftp/
Skripts atsevišķos threads iet cauri sarakstam un pieprasa pirmos 5 failus no FTP servera, ja tam ir iespējots anonīmā piekļuve


Piemērs: python d-FTPParser.py FTPList.txt
```
Apstrādā ftp.tu-chemnitz.de
Apstrādā ftp.tu-clausthal.de
Apstrādā ftp.tu-dresden.de
Apstrādā ftp.uakom.sk
Apstrādā ftp.uc.edu
Kļūda apstrādājot ftp.tu-dresden.de: [Errno 11001] getaddrinfo failed
Apstrādā ftp.uleth.ca
Kļūda apstrādājot ftp.uakom.sk: [Errno 11001] getaddrinfo failed
Apstrādā ftp.uncc.edu
Kļūda apstrādājot ftp.uc.edu: [Errno 11001] getaddrinfo failed
Apstrādā ftp.uni-erlangen.de
Pieslēdzās anonīmi: ftp.tu-chemnitz.de
Kļūda apstrādājot ftp.uncc.edu: [Errno 11001] getaddrinfo failed
Apstrādā ftp.uni-mainz.de
Pieslēdzās anonīmi: ftp.tu-clausthal.de
Pieslēdzās anonīmi: ftp.uni-erlangen.de
Kļūda apstrādājot ftp.uni-mainz.de: 530 Anonymous sessions must use encryption.
Apstrādā ftp.uni-trier.de
ftp.tu-chemnitz.de faili: ['INDEX', 'pub', 'test']
Kļūda apstrādājot ftp.uni-trier.de: [Errno 11001] getaddrinfo failed
Apstrādā ftp.unipv.it
ftp.tu-clausthal.de faili: ['lost+found', 'pub']
Apstrādā ftp.univ-rennes1.fr
Apstrādā ftp.up.ac.za
Kļūda apstrādājot ftp.unipv.it: [Errno 11001] getaddrinfo failed
Apstrādā 161.105.2.22
ftp.uni-erlangen.de faili: ['grml', 'apache', 'eclipse']
Apstrādā 199.3.234.248
Pieslēdzās anonīmi: ftp.up.ac.za
ftp.up.ac.za faili: ['README.html', 'mirrors', 'pub']
Apstrādā a.cs.uiuc.edu
```

- ja ir Errno 11001, tad lapa nav sasniedzama


Piemērs: python d-FTPParser.py FTPList.txt --numFiles 5
```
ftp.tu-chemnitz.de faili: ['INDEX', 'pub', 'test']
Apstrādā ftp.up.ac.za
ftp.tu-clausthal.de faili: ['lost+found', 'pub']
Apstrādā 161.105.2.22
ftp.uni-erlangen.de faili: ['grml', 'apache', 'eclipse', 'cdn.media.ccc.de', 'almalinux']
```
