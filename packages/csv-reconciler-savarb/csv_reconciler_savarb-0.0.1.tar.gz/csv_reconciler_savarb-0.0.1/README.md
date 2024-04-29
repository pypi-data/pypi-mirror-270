# CSV Reconciliation Challenge (Python CLI Application)

This repo contains a csv reconciliation application written in python. The application is reconciles a source and target csv using Python

## Run with Docker

```bash
$ docker build -f Dockerfile -t csv_reconciler:latest .

$ docker run -it -p 5001:5001 --name csv_reconciler csv_reconciler:latest

# Docker Docs: https://docs.docker.com/
# Docker Reference: https://docs.docker.com/reference/
```


## Run with Python

System Requirements: [Git](http://www.git-scm.com), [Python 3.8.0](https://www.python.org/downloads/)

```bash
# Check dependencies
$ git --version
git version 2.23.0

$ python --version
Python 3.8.0

$ pip --version # pip comes as a part of python install
pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)

# Clone the sourcecode
$ git clone <repo url>
$ cd <project dir>

# Install project dependencies
$ pip install -r requirements.txt

# Run the application
$ PORT=5001 python src/app.py

# Check application
$ curl http://localhost:5001/debug
# (or)
# In Browser visit -> http://localhost:5001/debug/ui
```

## Sample output

Pointing your browser to <http://localhost:5001/debug/ui> will bring up the following:

![](images/output.png)