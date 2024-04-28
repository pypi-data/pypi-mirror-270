import dns.resolver
import socket
import ipaddress
import argparse

class DNSAnalysis:
    def __init__(self, domain):
        self.domain = domain

    def fetch_domain_info(self):
        """Fetch general domain information."""
        try:
            result = dns.resolver.query(self.domain, 'ANY')
            domain_info = [f"Registrar: {result.registrar}"]
            domain_info.extend([f"{rdata}" for rdata in result])
            return domain_info
        except Exception as e:
            return ["Failed to fetch domain information:", str(e)]

    def reverse_dns_lookup(self, ip_address):
        """Perform reverse DNS lookup."""
        try:
            result = dns.resolver.resolve_address(ip_address)
            reverse_dns_info = [f"Reverse DNS: {result[0].to_text()}"]
            return reverse_dns_info
        except Exception as e:
            return ["Failed to perform reverse DNS lookup:", str(e)]

    def verify_dnssec(self):
        """Check DNSSEC."""
        try:
            result = dns.resolver.resolve(self.domain, 'DNSKEY')
            if result.response.flags & dns.flags.DO:
                return ["DNSSEC is enabled for", self.domain]
            else:
                return ["DNSSEC is not enabled for", self.domain]
        except Exception as e:
            return ["Failed to perform DNSSEC verification:", str(e)]

def main():
    parser = argparse.ArgumentParser(description="DNS Analysis")
    parser.add_argument("task", choices=["domain_info", "reverse_dns", "dnssec"], help="Task to perform")
    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument("--ip", help="IP address for reverse DNS lookup")
    args = parser.parse_args()

    if args.task == "domain_info":
        analysis = DNSAnalysis(args.target)
        domain_info = analysis.fetch_domain_info()
        for info in domain_info:
            print(info)
    elif args.task == "reverse_dns":
        analysis = DNSAnalysis(args.target)
        reverse_dns_info = analysis.reverse_dns_lookup(args.ip)
        for info in reverse_dns_info:
            print(info)
    elif args.task == "dnssec":
        analysis = DNSAnalysis(args.target)
        dnssec_info = analysis.verify_dnssec()
        for info in dnssec_info:
            print(info)

if __name__ == "__main__":
    main()
