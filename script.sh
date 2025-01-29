#!/bin/bash
oc label namespace openshift-gitops-operator openshift.io/cluster-monitoring=true
oc apply -f setup/namespace.yaml
oc project argo-rollouts
DOMAIN=$(oc get ingresses.config/cluster -o jsonpath='{.spec.domain}')
sed -i "s/<ingress-domain>/$DOMAIN/g" setup/error-app-service.yaml
oc apply -f setup/error-app-service.yaml
oc apply -f .
echo "Choose an app to roll out"
echo
echo
PS3="Enter your choice:"
options=("Healthy" "Error" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Healthy")
            echo "Rolling out healthy-app"
            sed -i "s/error-app:v4/healthy-app:v7/g" rollout.yaml
            oc apply -f rollout.yaml
            break
            ;;
        "Error")
            echo "Rolling out error-app"
            sed -i "s/healthy-app:v7/error-app:v4/g" rollout.yaml
            oc apply -f rollout.yaml
            break
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
sed -i "s/$DOMAIN/<ingress-domain>/g" setup/error-app-service.yaml
