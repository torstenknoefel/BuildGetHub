This image creates a python container, clones a github (python) repo, installs the requirements if any and runs a python file called "run-me.py"


## How does it work?
It’s simple. You HAVE to define the following environment variables:

```
REPO_URL:  Url of the GitHub repository  - no default - REQUIRED !!
REPO_BRANCH:  Repository branch which shall be cloned  - default: 'master'
BASE_DIR:  Directory for cloning the repository  - default: '~/repo'
```
In case the repository is private you need to specify credentials:
```
GIT_USERNAME
GIT_PASSWORD
```

To connect to docker you need to have the following 'bind mapping' volume:
```
Host/volume                                 Path in container
/var/run/docker.sock                        /var/run/docker.sock  
```


In addition you need to set ALL environment variables your repository (provided as REPO_URL) might require.
