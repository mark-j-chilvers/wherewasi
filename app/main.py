from flask import Flask, request
from kubernetes import client, config
app = Flask(__name__)

@app.route("/")
def lookupNodeName():
    nodeName = request.args.get('nodeName')

    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    v1 = client.CoreV1Api()
    

    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
