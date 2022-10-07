### Create ServiceAccount:
```sh
kubectl -n kube-system create serviceaccount <service-account-name>
```

### Create Secret
```sh
cat << EOF | kubectl create -f -
apiVersion: v1
kind: Secret
metadata:
  name: python-secret
  annotations:
    kubernetes.io/service-account.name: python-user
type: kubernetes.io/service-account-token
EOF
```

### Create ClusterRoleBinding and add an admin role (cluster-admin):
```sh
kubectl create clusterrolebinding <clusterrolebinding-name> --clusterrole=cluster-admin --serviceaccount=kube-system:<service-account-name>
```

### Get the secret name of the created ServiceAccount that stores the token
```sh
export TOKENNAME=$(kubectl -n kube-system get serviceaccount/<service-account-name> -o jsonpath='{.metadata.name}')
```

### Get the token from the secret in base64, decode it and add to the TOKEN environment variable:
```sh
export TOKEN=$(kubectl -n kube-system get secret $TOKENNAME -o jsonpath='{.data.token}' | base64 --decode)
```

### Make a request to the Kubernetes API:
```sh
curl -k -H "Authorization: Bearer $TOKEN" -X GET "https://<KUBE-API-IP>:6443/api/v1/nodes"
```

### Add the service account to kubeconfig:
```sh
kubectl config set-credentials <service-account-name> --token=$TOKEN
```

### Change the current context:
```sh
kubectl config set-context --current --user=<service-account-name>
```












