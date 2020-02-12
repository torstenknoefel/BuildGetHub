# Container which clones GitHub Repo and runs "runme"
#
# Version: XXXXXXX
FROM python:3

WORKDIR .

RUN apt-get update && apt-get install -y \
    git \
    python3-pip

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./run-github.py" ]
