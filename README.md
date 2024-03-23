# wherewasi

[work in progress!!]

This nginx sidecar and node-name lookup service can be used together in order to derive where (zone) a backend
service ran in a GKE cluster.

Deploy as a sidecar for your chosen backend service. It will add a header: `X-chili-wherewasi` with the name of the node
where the pod ran. Since downward API does not propagate the zone to the pod, this is best we can do.

This is then used in combination with a simple lookup service (in **app** folder) which leverages the Python kubernetes client
to lookup the node, and get the zone via the topology labels. This service can be deployed using yaml in the **deployapp** folder

Once deployed it can be called via `http://[IP]:8080?nodeName=[name-of-node]`

This service could be called via a service callout from the GCP LB.
