from kubernetes import client
import os

API_TOKEN = os.getenv("KIND_TOKEN", None)
API_URL   = "https://192.168.49.2:8443"

configuration = client.Configuration()
configuration.host = API_URL
configuration.ssl_ca_cert = "/home/daghan/.minikube/ca.crt"
configuration.verify_ssl = True
configuration.api_key = {"authorization": "Bearer " + API_TOKEN}
client.Configuration.set_default(configuration)
v1 = client.CoreV1Api()



print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))