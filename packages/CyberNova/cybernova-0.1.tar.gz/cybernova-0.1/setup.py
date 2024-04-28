from setuptools import setup, find_packages

setup(
    name='CyberNova',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'argparse',          # For command line parsing
        'dnspython',         # For DNS operations in dns_analysis.py
        'whois',             # For WHOIS lookups in ip_analysis.py
        'python-nmap',       # For port scanning and vulnerability checks
        'networkx',          # Optional, for network graphing if needed
        'matplotlib',        # Optional, for plotting if needed
        # Note: subprocess, os, ipaddress, socket are part of the standard library and need not be listed
    ],
    entry_points={
        'console_scripts': [
            'cybernova=CyberNova.cli:main',
            'cybernova-help=CyberNova.help:show_help'
        ]
    },
    author='Aniket Bhardwaj',
    author_email='aniket.bhardwaj0803@gmail.com',
    description='A package for cybersecurity analysis tools.',
    license='MIT',
    keywords='cybersecurity dns ssl port scanning vulnerability analysis',
)
