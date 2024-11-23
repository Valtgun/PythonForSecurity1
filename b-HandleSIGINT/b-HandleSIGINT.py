import time
import signal
import sys

# Funkcija ko izpildīs, kad saņems signālu
def handle_signal(signal, frame):
    print("\nGraceful - pareiza skripta pabeigšana.")
    sys.exit(0)

# SIGINT = Ctrl+C
signal.signal(signal.SIGINT, handle_signal)

# Ilgs process, kas jāapstādina, gaida ciklā 1 sekundi, līdz 10 sekundēm
def long_task():
    print("Sākt apstrādi. CTRL+C lai izietu")
    for i in range(10):
        time.sleep(1)
        print(f"{(i+1)*10}% pabeigts...", end='\r', flush=True)
    print("\nNepaspēji nospiest Ctrl+C.")


# MAIN
try:
    long_task()
except KeyboardInterrupt:
    print("\nPārtraukts, izgāja nekorekti!")

