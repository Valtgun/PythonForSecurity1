# Create TCP SYN network port scanner
pip3 install scapy

python e-PortScanner.py IP --port PortFrom PortTo

Ir iespējamas kļūdas, ja nelaiž admin režīmā dēļ drošības iestatījumiem
Uzrāda tikai aportus, kas snieguši atbildes

Piemērs: python e-PortScanner.py 127.0.0.1
```
Skanēt mērķi: 127.0.0.1 no porta: 1 līdz: 1024. Izmanto 6 procesus

Rezultāts:
Port 80: Open
Port 135: Open
Port 137: Filtered
Port 445: Open
Port 902: Open
Port 912: Open
```

Piemērs (Mikrotik): python e-PortScanner.py 192.168.8.1
```
Skanēt mērķi: 192.168.8.1 no porta: 1 līdz: 1024. Izmanto 6 procesus

Rezultāts:
Port 21: Open
Port 22: Open
Port 23: Open
Port 53: Open
Port 80: Open
Port 443: Open
```

Piemērs (RPi ar standarta KrakenDSR programmatūru, kurai uz 8080 un 8081 ir web serviss): 
python e-PortScanner.py 192.168.8.74
```
Skanēt mērķi: 192.168.8.74 no porta: 1 līdz: 1024. Izmanto 6 procesus

Rezultāts:
Port 22: Open
```

Piemērs (RPi ar standarta KrakenDSR programmatūru, kurai uz 8080 un 8081 ir web serviss): 
python e-PortScanner.py 192.168.8.74 --ports 8000 9000
```
Skanēt mērķi: 192.168.8.74 no porta: 8000 līdz: 9000. Izmanto 6 procesus

Rezultāts:
Port 8000: Open
Port 8042: Open
Port 8080: Open
Port 8081: Open
```
Izrādījās, ka uz 8042 porta ir ne pārāk plaši dokumentēts middleware serveris
