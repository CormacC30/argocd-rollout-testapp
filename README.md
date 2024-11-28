# A test application to demo canary deployments in a test environment

This is a simple application that runs in an OpenShift Cluster, to test Argo Rollouts canary deployments

# Set up

1. Clone repository

2. - Create `argo-rollouts` namespace: `oc new-project argo-rollouts` 
     
     OR

   - Adjust namespace field in each yaml file to desired project you wish to deploy in (if required) 

NOTE: leave `argo-rollouts-cluster-role.yaml`, `prometheus-role.yaml` and `prometheus-rolebinding.yaml` unchanged 

2. Ensure OpenShift GitOps operator is installed (logged as cluster administrator) you can do so by using the documentation below:

   https://docs.openshift.com/gitops/1.13/installing_gitops/installing-openshift-gitops.html#installing-openshift-gitops

   This can be done using web console OR if using the CLI:
   The required esources are already available in the "gitops-operator" directory. To install:
   - Run:

    ```
    cd gitops-operator 
    oc create ns openshift-gitops-operator
    ``` 

   - Enable cluster monitoring on openshift-gitops-operator namespace or any namespace it is required on:
     `oc label namespace <namespace> openshift.io/cluster-monitoring=true`
   - Apply resources to install operator: 
     `oc apply -f gitops-operator-group.yaml`
  
   - For a namespace-scoped argo rollouts installation:
    https://docs.openshift.com/gitops/1.14/argo_rollouts/enable-support-for-namespace-scoped-argo-rollouts-installation.html

     Set
     `oc apply -f subscription.yaml` 
     `oc apply -f rollout-manager.yaml`
   
   Check if all pods ar running successfully and `$ cd .. ` to parent directory


3. Ensure that the prometheus address is correct: Check prometheus-k8s service TCP port number `oc get svc prometheus-k8s -n openshift-monitoring` 

   And in analysisTemplate.yaml replace port number in `https://prometheus-k8s.openshift-monitoring.svc.cluster.local:<TCP port number>`


   Ensure prometheus TLS certificate is configured correctly, if using custom certificate

  ```
  oc create configmap prometheus-ca-cert \
  --from-file=ca.crt=/path/to/ca.crt \
  -n argo-rollouts
  ```


4. Apply each of the YAML manifests `oc apply -f .`

- Generate the Prometheus token:

  `oc create token prometheus-k8s -n openshift-monitoring` 

- Create the secret in argo-rollouts namespace (or whichever namespace you are running the rollout in) using token created above

  `oc create secret generic prometheus-token --from-literal=token=<TOKEN> -n argo-rollouts`

- The "healthy" app (which generates 200 status code) can has the following image: 

  `quay.io/rhn-support-ccostell/test-training/healthy-app:v7`

  The error-prone app (which randomly generates 500 status codes and delays) has the following image:

  `quay.io/rhn-support-ccostell/test-training/error-app:v4`

5. Replace the desired image (healthy or error prone above) in the .spec section of rollout.yaml for the app that is desired to be rolled out.

6. The status of the rollout can be monitored using `$ oc argo rollouts get rollout error-app-rollout --watch`