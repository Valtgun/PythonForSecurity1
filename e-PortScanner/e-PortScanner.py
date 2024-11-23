from scapy.all import sr1, IP, TCP
from multiprocessing import Pool, cpu_count
import argparse

# Skanē vienu mērķi un vienu portu
def scan_port(args):
    target, port = args
    try:
        # Build the TCP SYN packet
        syn_packet = IP(dst=target)/TCP(dport=port, flags='S') 
        response = sr1(syn_packet, timeout=1, verbose=0)
        if response:
            if response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK flag
                    return port, "Open"
                elif response[TCP].flags == 0x14:  # RST flag
                    return port, "Closed"
        return port, "Filtered"
    except Exception as e:
        return port, f"Error: {str(e)}"

# Daudzprocesu wrapperis
def scan_ports(target, ports, num_processes):
    # sagatavo visus ierakstus target, ports
    # [('127.0.0.1', 1), ('127.0.0.1', 2), ('127.0.0.1', 3), ('127.0.0.1', 4), ...
    args = [(target, port) for port in ports]
    
    # worker pool
    with Pool(processes=num_processes) as pool:
        results = pool.map(scan_port, args)
    return results

# MAIN
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP SYN network port scanner")
    parser.add_argument("target", type=str, help="Terget IP or host")
    parser.add_argument("--ports", type=int, nargs=2, default=[1, 1024], help="Scan range, array, e.g. [1, 1024]")
    parser.add_argument("--processes", type=int, default=cpu_count(), help="Number of processes")
    args = parser.parse_args()

    target = args.target
    port_range = range(args.ports[0], args.ports[1] + 1)
    num_processes = args.processes

    print(f"Skanēt mērķi: {target} no porta: {args.ports[0]} līdz: {args.ports[1]}. Izmanto {num_processes} procesus\n")

    # Perform the scan
    scan_results = scan_ports(target, port_range, num_processes)

    # Display results
    print("Rezultāts:")
    for port, status in scan_results:
        if status != "Closed":
            print(f"Port {port}: {status}")
