# A sample user application to demo canary deployments in a test environment

This is a simple application that runs in an OpenShift Cluster, to test Argo Rollouts canary deployments

## Set up

1. Clone repository: `git clone https://github.com/CormacC30/argocd-rollout-testapp` 

2. Navigate to the `argocd-rollouts-testapp` directory:

```
cd argocd-rollouts-testapp
```

2. Ensure OpenShift GitOps operator is installed (logged as cluster administrator) you can do so by using the documentation below:

   https://docs.openshift.com/gitops/1.13/installing_gitops/installing-openshift-gitops.html#installing-openshift-gitops

3. Enable cluster monitoring on openshift-gitops-operator namespace (or any namespace it is required on):

```
oc label namespace openshift-gitops-operator openshift.io/cluster-monitoring=true
```

4. Create the namespace, subscription and rolloutmanager, and change to the `argo-rollouts` namespace.

```
oc apply -f setup/namespace.yaml
oc project argo-rollouts
```

5. Get the ingress domain using:

```
oc get ingresses.config/cluster -o jsonpath='{.spec.domain}'
```

And add to the route object in error-app-service.yaml


```
oc apply -f setup/error-app-service.yaml
```

6. In **argo-rollouts-testapp root directory**,  apply each of the YAML manifests `oc apply -f .`

- Check if pods have successfully created: `oc get pods`

- Starting with the "healthy" app (which generates 200 status code) can has the following image: 

  `quay.io/rhn-support-ccostell/test-training/healthy-app:v7`

  Then roll out the error-prone app (which randomly generates 500 status codes and delays) has the following image:

  `quay.io/rhn-support-ccostell/test-training/error-app:v4`

7. Replace the desired image (healthy or error prone above) in the .spec section of rollout.yaml for the app that is desired to be rolled out.

8. The status of the rollout can be monitored using `$ oc argo rollouts get rollout error-app-rollout --watch`
