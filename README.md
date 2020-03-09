This image creates a python container, clones a github (python) repo, installs the requirements if any and runs a python file called "run-me.py"

How to install docker: https://docs.docker.com/install/linux/docker-ce/debian/

How to install Portainer: https://www.portainer.io/installation/

## How does it work?
It’s simple. You HAVE TO define the following environment variables:

```
REPO_URL:  Url of the GitHub repository  - no default - REQUIRED !!
```
To connect to docker you need to have the following bind mapping:
```
Host/volume                                 Path in container
/var/run/docker.sock                        /var/run/docker.sock  
```


In case the repository is private you need to specify credentials:
```
GIT_USERNAME
GIT_PASSWORD
```
You CAN set the following environment variables to change their default value:
```
REPO_BRANCH:  Repository branch which shall be cloned  - default: 'master'
BASE_DIR:  Directory for cloning the repository  - default: '~/repo'
```
In addition you need to set ALL environment variables your repository might require.

To watch the installation process the container writes to a log channel.


