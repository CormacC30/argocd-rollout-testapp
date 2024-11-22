# A test application to demo canary deployments in a test environment

This is a simple application that runs in an OpenShift Cluster, to test Argo Rollouts canary deployments

# Set up

1. Clone repository

2. - Create `argo-rollouts` namespace: `$ oc new-project argo-rollouts` 
     
     OR

   - Adjust namespace field in each yaml file to desired project you wish to deploy in (if required) 

NOTE: leave `argo-rollouts-cluster-role.yaml`, `prometheus-role.yaml` and `prometheus-rolebinding.yaml` unchanged 

2. Install Argo Rollouts controller

 `$ oc apply -f https://raw.githubusercontent.com/argoproj/argo-rollouts/v1.7.2/manifests/install.yaml -n argo-rollouts` 

3. Ensure that the prometheus address is correct: Check prometheus-k8s service TCP port number `oc get svc prometheus-k8s -n openshift-monitoring` 

   And in analysisTemplate.yaml replace port number in `https://prometheus-k8s.openshift-monitoring.svc.cluster.local:<TCP port number>`

4. Apply each of the YAML manifests `oc apply -f .`

- Generate the Prometheus token:

  `oc create token prometheus-k8s -n openshift-monitoring` 

- Create the secret in argo-rollouts namespace using token created above

  `oc create secret generic prometheus-token --from-literal=token=<TOKEN> -n argo-rollouts`

- The "healthy" app (which generates 200 status code) can has the following image: 

  `quay.io/rhn-support-ccostell/test-training/healthy-app:v7`

  The error-prone app (which randomly generates 500 status codes and delays) has the following image:

  `quay.io/rhn-support-ccostell/test-training/error-app:v4`

5. Replace the desired image (healthy or error prone above) in the .spec section of rollout.yaml for the app that is desired to be rolled out.

6. The status of the rollout can be monitored using `$ kubectl argo rollouts get rollout error-app-rollout --watch`