# MPI

mpiexec jaunākajām versijām ir cita sintakse
- Uzstādam https://www.microsoft.com/en-us/download/details.aspx?id=105289
- uz katra no datoriem palaižam smpd -d 0 vai smpd -d 2 ja vēlamies redzēt debug tekstus
- uz galvenā datora palaižam: mpiexec -hosts 1 localhost python f-DistributedMPI.py
- -hosts 1, uz cik datoriem palaidīsim paralēlo procesu
- nākamie aiz -hosts x ir hostname
- sosts failā abos datoros jāieliek abi ip/hostname
- pēc tam palaižamais process, piemēram:
- mpiexec -hosts 2 DESKTOP-60JQQA4 hostB python f-DistributedMPI.py

- Izskatās ka mpiexec strādā izmantojot AD kerberos autentifikāciju, nav iespējams palaist lokālā tīklā
Šo neizdevās novērst.

Kā alternatīvas tika apskatītas citas MPI implementācijas, bet tās nestrādā uz Windows.
Skaidra ir mērogošanas pieeja, bet šim risinājumam ir nepieciešama atbilstoša, sagatavota infrastruktūra.


Piemērs: python f-DistributedMPI
```
python f-DistributedMPI.py
Password found: hellow
Laiks: 89.40 sek, 1 procesi.
```
![1PC 1CPU](./images/pc1proc1.png)



```
mpiexec -n 6 python f-DistributedMPI.py
Password found: hellow
Laiks: 54.86 sek, 6 procesi.
```
![1PC 6CPU](./images/pc1proc6.png)


```
mpiexec -hostfile hostfile.txt -n 18 python f-DistributedMPI.py
```
Windows OS, mpiexec nestrādā, ja datori nav vienā domain.
OpenMPI, u.c. implementācijas, pamatā darbojas uz Linux, MacOS sistēmām. Šobrīd nav pieejamas vairākas šādas sistēmas, līdz ar to vairāku datoru testi nevar tikt veikti.


# MPI uz AWS

1. Konvertējam pem atslēgu uz ppk, izmantojot puttygen
2. Pieslēdzamies IP adresei izmantojot putty, norādot pie Connection->Data lietotājvārdu "ubuntu", un pie Connection->SSH->Auth 1.solī ģenerēto ppk.
3. Katram serverim, uzstādam openMPI:
```
sudo apt-get update
sudo apt-get install openmpi-bin libopenmpi-dev
mpiexec --version
sudo apt install python3-pip
sudo apt install python3-mpi4py
```
4. Izmantojot WinSCP nokopējam python failu uz serveri
5. Palaižam uz AWS: python3 f-DistributedMPI.py
```
Password found: hellow
Laiks: 98.60 sek, 1 procesi.
```
6. Ar lscpu, pārbaudam, ka ir 2 CPU pieejami
7. Palaižam mpirun -np 2 python f-DistributedMPI.py
```
Password found: hellow
Laiks: 182.56 sek, 2 procesi.
```

8. Uzstādam 2-7 uz otra hosta

9. Konfigurējam savienojumu:
```
ssh-keygen -t rsa
Pievienojam atslēgu pie authorized keys uz otra hosta
```

10. Konfigurējam hosts failu, un nokopējam uz galvenās mašīnas
11. Palaižam: mpirun --hostfile hostfile.txt -np 4 python f-DistributedMPI.py
```
Password found: hellow
Laiks: 103.38 sek, 4 procesi.
```


P.S.: Darbs tika veikts savā AWS kontā, jo iespējams pietrūka konfigurācija, ka visas instances atrodas vienā Subnet un starp instancēm nestrādāja, izmantojot iekšējās IP.
Pārbaudīt, ka strādā, tad var: mpirun --hostfile hostfile.txt -np 4 hostname
