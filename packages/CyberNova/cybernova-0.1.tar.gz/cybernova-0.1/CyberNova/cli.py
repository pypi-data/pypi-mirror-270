import argparse
from CyberNova.dns_analysis import DNSAnalysis
from CyberNova.ip_analysis import is_ip_up, whois_lookup, os_fingerprinting
from CyberNova.port_scanner import scan_port
from CyberNova.ssl_analysis import check_ssl_certificate
from CyberNova.vulnerability import scan_ports, scan_vulnerabilities

def create_parser():
    parser = argparse.ArgumentParser(description="CyberNova - Cybersecurity Toolkit")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # DNS Analysis
    dns_parser = subparsers.add_parser('dns_analysis', help='Perform DNS analysis')
    dns_parser.add_argument('task', choices=['domain_info', 'reverse_dns', 'dnssec'])
    dns_parser.add_argument('target', help='Target domain or IP address')

    # IP Analysis
    ip_parser = subparsers.add_parser('ip_analysis', help='Perform IP analysis')
    ip_parser.add_argument('task', choices=['is_ip_up', 'whois_lookup', 'os_fingerprinting'])
    ip_parser.add_argument('target', help='Target IP or domain')

    # Port Scanner
    port_parser = subparsers.add_parser('port_scanner', help='Scan ports')
    port_parser.add_argument('host', help='Host IP to scan')
    # You can add more options here as required

    # SSL Analysis
    ssl_parser = subparsers.add_parser('ssl_analysis', help='Check SSL certificate')
    ssl_parser.add_argument('domain', help='Domain to check')

    # Vulnerability Scanning
    vuln_parser = subparsers.add_parser('vulnerability', help='Perform vulnerability scanning')
    vuln_parser.add_argument('target_ip', help='Target IP to scan')

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'dns_analysis':
        dns = DNSAnalysis(args.target)
        if args.task == 'domain_info':
            print(dns.fetch_domain_info())
        elif args.task == 'reverse_dns':
            print(dns.reverse_dns_lookup(args.target))
        elif args.task == 'dnssec':
            print(dns.verify_dnssec())

    elif args.command == 'ip_analysis':
        if args.task == 'is_ip_up':
            print(is_ip_up(args.target))
        elif args.task == 'whois_lookup':
            print(whois_lookup(args.target))
        elif args.task == 'os_fingerprinting':
            print(os_fingerprinting(args.target))

    elif args.command == 'port_scanner':
        print(scan_port(args.host, args.port))  # Adjust this call according to actual function signature

    elif args.command == 'ssl_analysis':
        print(check_ssl_certificate(args.domain))

    elif args.command == 'vulnerability':
        open_ports = scan_ports(args.target_ip)
        scan_vulnerabilities(args.target_ip, open_ports)

if __name__ == "__main__":
    main()
