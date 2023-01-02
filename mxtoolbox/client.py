# mxtoolbox_api.py
import os
import httpx
import logging

logger = logging.getLogger("__name__")
logger.setLevel(logging.INFO)

valid_commands = {
    "mx": "Get MX DNS record.",
    "a": "Get A DNS record.",
    "dns": "Get DNS report for the domain.",
    "spf": "Get SPF DNS record.",
    "txt": "Get TXT record.",
    "soa": "Get SOA record.",
    "ptr": "Get PTR record.",
    "blacklist": "Check blacklists for given domain/IP.",
    "smtp": "Perform SMTP service check for given domain/IP.",
    "tcp": "TCP port check.",
    "http": "HTTP port check.",
    "https": "HTTPS port check.",
    "ping": "Ping check.",
    "trace": "Traceroute.",
    "dmarc": "Check DMARC record of domain.",
}

class MXToolBoxClient():
    def __init__(self, api_key: str = ""):
        self.apiUrl: str = "https://api.mxtoolbox.com/api/v1/Lookup"
        self.apiKey: str = os.environ.get("MXTOOLBOX_API_KEY", "")
        if (not self.apiKey) and api_key:
            self.apiKey = api_key
        self.validCommands: List = valid_commands.keys()
        if not self.apiKey:
            logger.error("API key not provided.")
        else:
            self.headers = {
                "Authorization": self.apiKey,
                "Content-Type": "application/json"
            }
        self.response = None

    def lookup(self, domain: str = "", command: str = "mx"):
        if not domain:
            logger.error("No domain provided.")
            return {}
        if not command:
            logger.error("No command query provided.")
            return {}
        if command not in self.validCommands:
            logger.error("Provided command is not in list of valid commands.")
            return {}
        self.response = httpx.get(
            f"{self.apiUrl}/{command}/{domain}",
            headers=self.headers)
        if self.response.status_code == 200:
            return self.response.json()
        else:
            logger.info(f"Received status code {self.response.status_code} while querying \"{domain}\" with command \"{command}\"")
            return {}
