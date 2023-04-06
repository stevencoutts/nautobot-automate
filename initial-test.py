import requests
import secret

host = "127.0.0.1"
port = "8443"

url = "api/tenancy/tenant-groups/"

request_url = "https://" + host + ":" + port + "/" + url
print (request_url)

headers = {"Authorization":"Token " + secret.api_key}
response = requests.get(request_url, headers=headers, verify=False)
print (response.status_code)
print (response.json())


