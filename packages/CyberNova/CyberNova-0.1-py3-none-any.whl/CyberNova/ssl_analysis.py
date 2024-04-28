import subprocess
import os
import argparse
import sys
def check_ssl_certificate(domain):
    """Check SSL/TLS certificate details for a domain."""
    try:
        print("Checking SSL/TLS certificate details for:", domain)
        if os.system(f"openssl s_client -connect {domain}:443 -showcerts") != 0:
            raise Exception("OpenSSL command failed.")
    except Exception as e:
        print("Error:", e)


def main():
    parser = argparse.ArgumentParser(description="Check SSL/TLS certificate details for a domain")
    parser.add_argument("domain", help="Domain to check SSL certificate details")
    args = parser.parse_args()

    result = check_ssl_certificate(args.domain)
    if result:
        print(result)
    
    # Wait for user input before exiting
    input("Press Enter to exit...")
    sys.exit(0)

if __name__ == "__main__":
    main()