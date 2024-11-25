# Create FTP site parser

FTP linki paņemti no http://www.diam.unige.it/informatica/documentazione/httpd_docs/ftp/
Skripts atsevišķos threads iet cauri sarakstam un pieprasa pirmos 5 failus no FTP servera, ja tam ir iespējots anonīmā piekļuve

## using Google Gemini GPT
pip3 install google-generativeai
piereģistrēties atbilstoši instrukcijai, t.sk API key: https://ai.google.dev/api?lang=python
export API_KEY=<YOUR_API_KEY>
(set) for Windows

Pabeidzot darbu uzrādās divi ieraksti, kas ir no Google Gemini API, var ignorēt:
```
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1732551783.383549    8520 init.cc:229] grpc_wait_for_shutdown_with_timeout() timed out.
```


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


## Tā, ka Google API ir mainīts, tad domāju izmantot jaunāku API, bet interesantāk bija pamēģināt izmantot Google GPT (Gemini), lai palīdzētu risināt šo jautājumu

Ja ir failā norādīts mazāk nekā vajadzīgais FTP saitu skaiuts, tad tiek nosūtīts prompt ar esošajiem, lūdzot atsūtīt jaunos, tādejādi vaidojot uzreiz arī filtrāciju:

python d-FTPParser.py FTPGemini.txt
```
I need to have additional 15 FTP sites, that are not listed in the following list: ['speedtest.tele2.net', 'speedtest.qwest.net', 'speedtest.l2.com2', 'ftp.kernel.org', 'ftp.gnu.org']. Please provide them without leading ftp:// and give them in format that has each FTP separated with newline character
speedtest.comcast.net
speedtest.earthlink.net
speedtest.cox.net
speedtest.verizon.net
speedtest.charter.net
speedtest.at&t.net
speed.io
ftp.ncbi.nlm.nih.gov
ftp.mozilla.org
ftp.icann.org
ftp.acc.umu.se
ftp.sunet.se
ftp.cs.huji.ac.il
ftp.fau.edu
mirror.umd.edu

Apstrādā speedtest.tele2.net
Apstrādā speedtest.qwest.netApstrādā speedtest.l2.com2

Apstrādā ftp.kernel.org
Apstrādā ftp.gnu.org
Kļūda apstrādājot speedtest.l2.com2: [Errno 11001] getaddrinfo failed
Apstrādā speedtest.comcast.net
Kļūda apstrādājot ftp.kernel.org: [Errno 11001] getaddrinfo failed
Apstrādā speedtest.earthlink.net
Pieslēdzās anonīmi: speedtest.tele2.net
Kļūda apstrādājot speedtest.qwest.net: [WinError 10054] An existing connection was forcibly closed by the remote host

Apstrādā speedtest.cox.net
speedtest.tele2.net faili: ['1000GB.zip', '100GB.zip', '100KB.zip']

Apstrādā speedtest.verizon.net
Kļūda apstrādājot speedtest.cox.net: [Errno 11001] getaddrinfo failed
Apstrādā speedtest.charter.net
Kļūda apstrādājot speedtest.comcast.net: [Errno 11001] getaddrinfo failed
Apstrādā speedtest.at&t.net
Kļūda apstrādājot speedtest.at&t.net: [Errno 11001] getaddrinfo failed
Apstrādā speed.io
Kļūda apstrādājot speedtest.charter.net: [Errno 11001] getaddrinfo failed
Apstrādā ftp.ncbi.nlm.nih.gov
Pieslēdzās anonīmi: ftp.gnu.org
Pieslēdzās anonīmi: ftp.ncbi.nlm.nih.gov

ftp.gnu.org faili: ['CRYPTO.README', 'MISSING-FILES', 'MISSING-FILES.README']
Apstrādā ftp.mozilla.org
ftp.ncbi.nlm.nih.gov faili: ['bioproject', 'hmm', 'refseq']

Apstrādā ftp.icann.org
Kļūda apstrādājot ftp.icann.org: [Errno 11001] getaddrinfo failed
Apstrādā ftp.acc.umu.se
Pieslēdzās anonīmi: ftp.acc.umu.se
Kļūda apstrādājot ftp.acc.umu.se: 550 Permission denied.
Apstrādā ftp.sunet.se
Pieslēdzās anonīmi: ftp.sunet.se
Kļūda apstrādājot ftp.sunet.se: 550 Permission denied.
Apstrādā ftp.cs.huji.ac.il
Kļūda apstrādājot speedtest.earthlink.net: timed out
Apstrādā ftp.fau.edu
Kļūda apstrādājot ftp.fau.edu: [Errno 11001] getaddrinfo failed
Apstrādā mirror.umd.edu
Kļūda apstrādājot speedtest.verizon.net: timed out
Kļūda apstrādājot speed.io: timed out
Kļūda apstrādājot ftp.mozilla.org: timed out
Kļūda apstrādājot ftp.cs.huji.ac.il: timed out
Kļūda apstrādājot mirror.umd.edu: timed out
----- Done -----
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1732551783.383549    8520 init.cc:229] grpc_wait_for_shutdown_with_timeout() timed out.
```