
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from checker import build_url, is_https, show_response, check_site, scan_sites, check_headers, retry_check

#Partea 1

print("Functia build_url:", build_url("www.example.com", "/login"))  
print("Functia build_url:", build_url("https://httpbin.org", "/html")) 

print("Functia is_https:", is_https("https://www.example.com"))
print("Functia is_https:", is_https("http://httpbin.org/status/500"))

#Partea 2 
print("Functia show_response:", show_response("https://httpbin.org/html"))
print("Functia show_response:", show_response("https://httpbin.org/response-headers?x-frame-options=DENY"))

#Partea 3 
print("Functia check_site:", check_site("https://example.com"))
print("Functia check_site:", check_site("https://httpbin.org/html"))

#Partea 4
print("Functia scan_sites:", scan_sites())

#Partea 5
print("Functia check_headers:", check_headers("https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff"))  
print("Functia check_headers:", check_headers("https://httpbin.org/response-headers?x-frame-options=DENY"))

#Partea 6
print("Functia retry_check:", retry_check("https://httpbin.org/status/200,500", 3))
print("Functia retry_check:", retry_check("http://this-site-does-not-exist.invalid", 3))