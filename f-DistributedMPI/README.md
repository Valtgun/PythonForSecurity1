# Create TCP SYN network port scanner

TODO:
- description
- mpiexec newer version does not support hostfile, need to check
- mpiexec documentation to be found


python f-DistributedMPI 


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
![xPC xCPU](./images/pc1proc6.png)



