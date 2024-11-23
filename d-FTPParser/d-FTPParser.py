import ftplib
import os
import argparse
import threading
import queue
#from googlesearch import search
from urllib.parse import urlparse

# def ftp_file_check(file, sites=20):
# -----------------------------------------------
# Jāpārraksta funkcija, jo googlesearch neatbalsta lapošanu un pygoogle neuzstādījās korekti
# FTP linki paņemti no http://www.diam.unige.it/informatica/documentazione/httpd_docs/ftp/
# -----------------------------------------------
#     ftp_sites = []
#     results_per_page = 50
#     page = 1

#     with open(file, "r+") as file:
#         ftp_sites = [line.strip() for line in file.readlines()]
#         while len(ftp_sites)<sites:
#             query = "inurl:ftp -inurl:(http|https)"
#             search_results = search(query, num_results=results_per_page, sleep_interval=5)
#             for url in search_results:
#                 parsed_url = urlparse(url)
#                 domain = parsed_url.netloc
#                 if (domain in ftp_sites):
#                     print(f"Duplicate found, in list # items: {len(ftp_sites)}")
#                 else:
#                     file.write(domain + "\n")
#                     ftp_sites.append(domain)
#     return ftp_sites

# Worker thread klase
class WorkerThread(threading.Thread):
    def __init__(self, queue, n_files=3):
        threading.Thread.__init__(self)
        self.queue = queue
        self.n_files = n_files

    def run(self):
        while not self.queue.empty():
            site = self.queue.get()
            print(f"Apstrādā {site}")
            self.process_ftp_site(site)
            self.queue.task_done()

    def process_ftp_site(self, site):
        try:
            ftp = ftplib.FTP(site, timeout=10)
            ftp.login()  # Try anonymous login
            print(f"Pieslēdzās anonīmi: {site}")

            ftp.cwd('/')
            file_list = ftp.nlst()[:self.n_files]
            print(f"{site} faili: {file_list}")

            ftp.quit()
        except Exception as e:
            print(f"Kļūda apstrādājot {site}: {e}")

def ftp_getter(file, numThreads, numFiles):
    if os.path.exists(file):
        with open(file, "r") as file:
            ftp_sites = [line.strip() for line in file.readlines()]
    q = queue.Queue()
    for site in ftp_sites:
        q.put(site)
    threads = []
    for _ in range(numThreads):
        worker = WorkerThread(q, n_files=numFiles)
        worker.start()
        threads.append(worker)
    
    for worker in threads:
        worker.join()
    print("----- Done -----")
   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pārlūkot FTP saitus")
    parser.add_argument("file", help="Fails, kas satur ftp lapas, ja tukšs vai nav aizpildīts, tad izveidos failu")
    parser.add_argument("--threads", nargs='?', const=5, default=5, help="Palalēlie izpildes threads skaits")
    parser.add_argument("--sites", nargs='?', const=20, default=20, help="Cik FTP saitus apmeklēt")
    parser.add_argument("--numFiles", nargs='?', const=3, default=3, help="Cik failus katrā FTP saitā sameklēt")
    args = parser.parse_args()
    #ftp_sites = ftp_file_check(args.file, args.sites)
    ftp_getter(args.file, int(args.threads), int(args.numFiles))