# A sample user application to demo canary deployments in a test environment

This is a simple application that runs in an OpenShift Cluster, to test Argo Rollouts canary deployments

## Set up

1. Clone repository: `git clone https://github.com/CormacC30/argocd-rollout-testapp` 

2. Navigate to the `argocd-rollouts-testapp` directory:

```
cd argocd-rollouts-testapp
```

3. Ensure OpenShift GitOps operator is installed (logged as cluster administrator) you can do so by using the documentation below:

   https://docs.openshift.com/gitops/1.13/installing_gitops/installing-openshift-gitops.html#installing-openshift-gitops

4. Ensure script.sh is executable

```
chmod +x script.sh
```

5. Execute script.sh to start rollout

```
./script.sh
```

6. To test healthy or error-prone apps, execute script again and choose appropriate option.