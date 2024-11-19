# A test application to demo canary deployments in test environment

This is a simple application that runs in an OpenShift Cluster, to test Argo Rollouts canary deployments

# Set up

- Apply each of the YAML manifests to enable all the correct roles and rolebindings using `oc apply -f <filename>`

- Generate the Prometheus token:

  `oc create token prometheus-k8s -n openshift-monitoring` 

- Create the secret in argo-rollouts namespace using token created above

  `oc create secret generic prometheus-token --from-literal=token=<TOKEN> -n argo-rollouts`

- The "healthy" app (which generates 200 status code) can has the following image: 

  `quay.io/rhn-support-ccostell/test-training/healthy-app:v7`

  The error-prone app (which randomly generates 500 status codes and delays) has the following image:

  `quay.io/rhn-support-ccostell/test-training/error-app:v4`

- Replace the desired image (healthy or error prone above) in the .spec section of rollout.yaml for the app that is      desired to be rolled out.

The status of the rollout can be monitored using `$ kubectl argo rollouts get rollout error-app-rollout --watch`