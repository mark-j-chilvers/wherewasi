from flask import Flask, request
from kubernetes import client, config
app = Flask(__name__)

@app.route("/")
def lookupNodeName():
    nodeName = request.args.get('nodeName')
    print ('Node name: ', nodeName)
    # Configs can be set in Configuration class directly or using helper utility

    config.load_incluster_config()

    v1 = client.CoreV1Api()
    ret = v1.read_node(name=nodeName, async_req=False)
    # topology.kubernetes.io/zone   
    print('return: ', ret)
    return ret.get('metadata').get('labels')['topology.kubenetes.io/zone']

if __name__ == "__main__":
    app.run(host='0.0.0.0')
