import socket 
import argparse 
import ipaddress 
import os


def scan_port(host, port):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            sock.settimeout(1)
            # Attempt to connect to the specified host and port
            result = sock.connect_ex((host, port))
            # Check if the connection was successful
            if result == 0:
                return f"Port {port} is open"
            else:
                return f"Port {port} is closed"
            # Close the socket
            sock.close()
        except socket.error as e:
            return f"Error: {e}"


def main():
        parser = argparse.ArgumentParser(description="TCP Port Scanner")
        parser.add_argument("host", help="Target host or IP address")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("-p", "--ports", nargs="+", type=int, help="Individual ports to scan")
        group.add_argument("-r", "--range", nargs=2, type=int, help="Range of ports to scan (start end)")
        group.add_argument("-c", "--complete", action="store_true", help="Scan all well-known ports (0-1023)")
        args = parser.parse_args()

        # Check if the input is an IP address
        try:
            ipaddress.ip_address(args.host)
            is_ip = True
        except ValueError:
            is_ip = False

        host = args.host
        if args.ports:
            ports = args.ports
        elif args.range:
            start_port, end_port = args.range
            ports = list(range(start_port, end_port + 1))
        else:
            ports = range(1024)  # Well-known ports

        if args.complete:
            ports.extend(range(1024, 65536))  # Optionally scan higher ports

        results = []
        for port in ports:
            result = scan_port(host, port)
            results.append(result)

        save_results = input("Do you want to save the results? (yes/no): ").lower() == "yes"
        if save_results:
            output_dir = input("Enter the path where you want to save the results: ")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            if is_ip:
                filename = f"{host}_ports.txt"
            else:
                filename = f"{host.replace('.', '_')}_ports.txt"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w") as f:
                f.write("\n".join(results))
                print(f"Results saved to {filepath}")
        else:
            print("\n".join(results))

if __name__ == "__main__":
    main()