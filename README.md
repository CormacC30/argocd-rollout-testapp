# A sample user application to demo canary deployments in a test environment

This is a simple application that runs in an OpenShift Cluster, to test Argo Rollouts canary deployments

## Set up

1. Clone repository: `git clone https://github.com/CormacC30/argocd-rollout-testapp` 

2. - Create argo-rollouts namespace: `oc new-project argo-rollouts` 
     
     OR

   - Adjust namespace "argo-rollouts" to your desired namespace

2. Ensure OpenShift GitOps operator is installed (logged as cluster administrator) you can do so by using the documentation below:

   https://docs.openshift.com/gitops/1.13/installing_gitops/installing-openshift-gitops.html#installing-openshift-gitops

   - Run:

    ```
    cd gitops-operator 

    ``` 

   - Enable cluster monitoring on openshift-gitops-operator namespace or any namespace it is required on:

     ```
     oc label namespace <namespace> openshift.io/cluster-monitoring=true
     ```

   - Apply resources to install operator: 

     ```
     oc apply -f gitops-operator-group.yaml
     ```
  
   - For a namespace-scoped argo rollouts installation:
    https://docs.openshift.com/gitops/1.14/argo_rollouts/enable-support-for-namespace-scoped-argo-rollouts-installation.html

     Set
     `oc apply -f subscription.yaml` 
     `oc apply -f rollout-manager.yaml`
   
   Check if all pods ar running successfully and `$ cd .. ` to parent directory

3. In analysis template change the prometheus query address to one for the required environment.
   Run the following commands:

```
oc get route thanos-querier -n openshift-monitoring -o jsonpath='{.spec.host}'
```

Replace the prometheus addres in `analysisTemplate.yaml` in `.spec.metrics.provider.prometheus.address`

4. In **argo-rollouts-testapp root directory**,  apply each of the YAML manifests `oc apply -f .`

- The "healthy" app (which generates 200 status code) can has the following image: 

  `quay.io/rhn-support-ccostell/test-training/healthy-app:v7`

  The error-prone app (which randomly generates 500 status codes and delays) has the following image:

  `quay.io/rhn-support-ccostell/test-training/error-app:v4`

5. Replace the desired image (healthy or error prone above) in the .spec section of rollout.yaml for the app that is desired to be rolled out.

6. The status of the rollout can be monitored using `$ oc argo rollouts get rollout error-app-rollout --watch`