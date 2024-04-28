def show_help():
    help_text = """
CyberNova - A Comprehensive Cybersecurity Toolkit

Usage:
    cybernova <command> [options]

Commands:
    dns_analysis    - Perform DNS analysis tasks such as domain information retrieval, reverse DNS, and DNSSEC verification.
        Usage: cybernova dns_analysis <task> <target>
        Tasks:
            domain_info    - Fetch domain information.
            reverse_dns    - Perform a reverse DNS lookup.
            dnssec         - Verify DNSSEC implementation.

    ip_analysis     - Perform IP related analyses including IP status check and WHOIS lookups.
        Usage: cybernova ip_analysis <task> <target>
        Tasks:
            is_ip_up       - Check if an IP address is up.
            whois_lookup   - Perform a WHOIS lookup.
            os_fingerprinting - Fingerprint the operating system of a host.

    port_scanner    - Scan ports on a specified IP address.
        Usage: cybernova port_scanner <host>

    ssl_analysis    - Check SSL/TLS certificate details for a domain.
        Usage: cybernova ssl_analysis <domain>

    vulnerability   - Scan for vulnerabilities on open ports of a target IP.
        Usage: cybernova vulnerability <target_ip>

Examples:
    cybernova dns_analysis domain_info example.com
    cybernova ip_analysis is_ip_up 192.168.1.1
    cybernova port_scanner 192.168.1.1
    cybernova ssl_analysis example.com
    cybernova vulnerability 192.168.1.1

Type 'cybernova <command> --help' for more details on a specific command.
    """
    print(help_text)

if __name__ == "__main__":
    show_help()
