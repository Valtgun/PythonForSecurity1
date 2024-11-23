import re
import argparse

def filter_logs(file, keyword, pattern=None):
    """
    Funkcija, kas filtrē log faila rindas
    
    Ievaddati:
        file (str): Faila atrašanās vieta
        keyword (str): Atslēgas vārs pēc kura filtrēt faila rindas
        pattern (str): Regex izteiksme, kas attēlos izvadā pēc noteiktā pattern, ja nav norādīts, tad izdrukā visu rindu

    Izvaddati:
        Nav
    """
    try:
        with open(file, 'r') as file:
            print(f"Fails: {file}")
            for line in file:
                if keyword in line:
                    if pattern:
                        match = re.search(pattern, line)
                        if match:
                            print(match.group())
                        else:
                            print(f"Neatrada regex atbilstošu pattern : {line.strip()}")
                    else:
                        print(line.strip())
    except FileNotFoundError:
        print(f"Error: Fails nav atrasts '{file}'")
    except Exception as e:
        print(f"Exception: An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meklēt failā atbistošu atslēgas vārdu")
    parser.add_argument("file", help="Faila ceļš un nosaukums")
    parser.add_argument("keyword", help="Atslēgas vārds pēc kura filtrēt faila rindas")
    parser.add_argument("--pattern", help="Regex pattern pēc kura izvadīt rezultātu, piem \d{4}-\d{2}-\d{2}")
    args = parser.parse_args()

    filter_logs(args.file, args.keyword, args.pattern)
