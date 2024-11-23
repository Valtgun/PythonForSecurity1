import sys
import urllib.request
import argparse
import signal

def handle_signal(signal, frame):
    sys.stdout.flush() # novērš kļūdu, ka callback funkcija mēģina izmantot stdout bufferi
    print("\nPārtrauc ielādi, daļēji ielādēts fails netika izdzēsts.")
    sys.exit(0)
signal.signal(signal.SIGINT, handle_signal)

# Callback funkcija, kas ir pielikta pie urlretrieve, kā hook
def progress(block_num, block_size, total_size):
    completed = block_num * block_size
    percent = completed / total_size * 100
    print(f"Pabeigts: {percent:.2f}% no {total_size/1024/1024:.0f}Mb\r", end="")

def download_file(file):
    try:
        print(f"sāk ielādēt {file}...")
        urllib.request.urlretrieve(file, "fails.download", reporthook=progress)
        print(f"\nPielādēšana pabeigta!")
    except Exception as e:
        print(f"Kļūda! {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Novilkt failu no interneta")
    parser.add_argument("file", help="Faila URL")
    args = parser.parse_args()
    download_file(args.file)