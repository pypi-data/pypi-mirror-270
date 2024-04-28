# CyberNova

CyberNova is a comprehensive cybersecurity toolkit designed for performing network analysis, port scanning, DNS audits, SSL certificate checks, and vulnerability assessments. It aims to provide security professionals and researchers with an efficient tool for active reconnaissance and preliminary vulnerability detection.

## Features

- **DNS Analysis**: Retrieve DNS records, perform reverse DNS lookups, and verify DNSSEC implementations.
- **IP Analysis**: Check if IP addresses are up, perform WHOIS lookups, and deduce operating systems based on IP response behaviors.
- **SSL/TLS Certificate Checks**: Analyze SSL/TLS certificates for any domain to ensure encryption security.
- **Port Scanning**: Efficiently scan ports to determine open services and potential points of vulnerability.
- **Vulnerability Scanning**: Leverage open ports to detect possible vulnerabilities that could be exploited.

## Installation

CyberNova is designed to work on Linux and macOS operating systems. Installation on other operating systems is not currently supported.





## Usage

Once installed, you can run CyberNova directly from the command line:

cybernova --help

To perform a specific task, use one of the following commands:

cybernova dns\_analysis --domain example.com

cybernova ip\_analysis --target 192.168.1.1

cybernova ssl\_check --domain example.com

cybernova port\_scan --host 192.168.1.1

cybernova vulnerability\_scan --target 192.168.1.1

## Contributing

Contributions to CyberNova are welcome! Please consider the following ways to contribute:

Report Bugs: Use the GitHub Issues section to report a bug.

Feature Requests: Have an idea that could make CyberNova better? Open an issue and tell us about it.

Code Contributions: Submit a pull request with your improvements or new features.

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests to us.

## Authors

Aniket Bhardwaj - Initial work - Aniket Bhardwaj

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact

If you have any questions, you can reach out by sending an email to

aniket.bhardwaj0803@gmail.com.
