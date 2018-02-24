


## Troubleshooting Errors

```
(microflask_env) cliffs-MacBook-Pro:testdriven-app connie$ docker-machine create -d virtualbox microflask-dev
Creating CA: /Users/connie/.docker/machine/certs/ca.pem
Creating client certificate: /Users/connie/.docker/machine/certs/cert.pem
Running pre-create checks...
Error with pre-create check: "VBoxManage not found. Make sure VirtualBox is installed and VBoxManage is in the path"
```

Make sure to install VirtualBox. Download binaries here: https://www.virtualbox.org/wiki/Downloads

For MacOS, you may encounter Installation Failed error. See: https://stackoverflow.com/questions/46546192/virtualbox-not-installing-on-high-sierra
