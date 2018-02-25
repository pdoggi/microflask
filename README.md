# Microservices with Docker, Flask, and React

This is just my repo with notes from the book, Microservices with Docker, Flask, and React by Michael Herman from https://testdriven.io/.

Original repo: https://github.com/testdrivenio/testdriven-app-2.2

## Handy Docker commands

To clear containers:
```
docker rm -f $(docker ps -a -q)
```
To clear images:
```
docker rmi -f $(docker images -a -q)
```
To clear volumes:
```
docker volume rm $(docker volume ls -q)
```
To clear networks:
```
docker network rm $(docker network ls | tail -n+2 | awk '{if($2 !~ /bridge|none|host/){ print $1 }}')
```

To connect to postgres:
```
docker exec -ti $(docker ps -aqf "name=users-db") psql -U postgres
```

## Tips & Tricks

When you add dependencies, you need to rebuild images since requirements are installed at build time, not run time.

## Troubleshooting Errors

```
(microflask_env) $ docker-machine create -d virtualbox microflask-dev
Creating CA: /Users/your_username/.docker/machine/certs/ca.pem
Creating client certificate: /Users/your_username/.docker/machine/certs/cert.pem
Running pre-create checks...
Error with pre-create check: "VBoxManage not found. Make sure VirtualBox is installed and VBoxManage is in the path"
```

Make sure to install VirtualBox. Download binaries here: https://www.virtualbox.org/wiki/Downloads

For MacOS, you may encounter Installation Failed error. See: https://stackoverflow.com/questions/46546192/virtualbox-not-installing-on-high-sierra
