import subprocess
import whois
import re
import argparse

def is_ip_up(ip_address):
    try:
        subprocess.run(["ping", "-c", "1", "-W", "2", ip_address], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def whois_lookup(domain):
    try:
        # Perform WHOIS lookup
        domain_info = whois.whois(domain)
        # Check if WHOIS lookup was successful
        if domain_info:
            return domain_info
        else:
            return "WHOIS information not found for this domain."
    except Exception as e:
        return f"Error: {str(e)}"

def os_fingerprinting(ip_address):
    try:
        # Send ping request to the target system and capture the output
        result = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True, text=True)
        print("Ping Output:", result.stdout)  # Print the output for debugging
        # Extract TTL value from the output using regular expression
        ttl_match = re.search(r"ttl=(\d+)", result.stdout, re.IGNORECASE)
        print("TTL Match:", ttl_match)  # Print the ttl_match for debugging
        if ttl_match:
            ttl = int(ttl_match.group(1))
            print("TTL:", ttl)  # Print the TTL value for debugging
            # Perform OS inference based on TTL value
            if 0 < ttl <= 64:
                return "Likely Linux/Unix"
            elif 64 < ttl <= 128:
                return "Likely Windows"
            elif ttl > 128:
                return "Likely Solaris/AIX"
            else:
                return "Unable to determine OS"
    except subprocess.CalledProcessError:
        return "Error: Unable to send ping request"

def main():
    parser = argparse.ArgumentParser(description="Network Analysis Tool")
    parser.add_argument("task", choices=["is_ip_up", "whois_lookup", "os_fingerprinting"], help="Task to perform")
    parser.add_argument("target", help="Target domain or IP address")
    args = parser.parse_args()

    if args.task == "is_ip_up":
        result = is_ip_up(args.target)
        print(f"The IP address {args.target} is {'up' if result else 'down'}")
    elif args.task == "whois_lookup":
        result = whois_lookup(args.target)
        print(result)
    elif args.task == "os_fingerprinting":
        result = os_fingerprinting(args.target)
        print(f"The OS for IP address {args.target} is {result}")

if __name__ == "__main__":
    main()
