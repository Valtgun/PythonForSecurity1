import os
import argparse

def traverse(path, args, level=0):
    """
    Funkcija, kas rekursīvi parāda failus katalogā
    
    Ievaddati:
        path (str): Sākotnējā atrašanās vieta no kuras sākt skanēšanu
        args (): Ja norādīts, tad rādīs parametrus atrastajiem failiem

    Izvaddati:
        Nav
    """
    try:
        with os.scandir(path) as objects:
            for object in objects:
                if args and object.is_file():
                    attribs = os.stat(object.path)
                    if hasattr(attribs, 'st_birthtime'):
                        created_time = attribs.st_birthtime
                    else:
                        created_time = attribs.st_ctime
                    print("|-"+"----" * level + object.name + " Size:" + str(attribs.st_size) + " Created:"+ str(created_time) + " Permissions:" + str(oct(attribs.st_mode)))
                else:
                    print("|-"+"----" * level + object.name)
                    if object.is_dir():
                        traverse(object.path, args, level+1)
    except Exception as e:
        print(f"Exception: An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skanē rekursīvi diska katalogu un atrāda visiem failiem atribūtus")
    parser.add_argument("path", help="Čeļš uz sākotnējo kataloga atrašanās vietu")
    parser.add_argument("--a", nargs='?', const=True, default=False, help="Ja norādīts, tad drukāt faila atribūtus")
    args = parser.parse_args()

    traverse(args.path, args.a)
