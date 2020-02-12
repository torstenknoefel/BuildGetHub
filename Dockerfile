# Container which clones GitHub Repo and runs "runme"
#
# Version: XXXXXXX
FROM python

WORKDIR .

RUN apt-get update && apt-get install -y \
    git

#COPY requirements.txt ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./run-github.py" ]
