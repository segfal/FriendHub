FROM postgres:14
#enviorment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres

EXPOSE 5432
WORKDIR /root/backend
COPY app.py root/app.py
COPY dbase.py root/dbase.py
COPY encryption.py root/encryption.py
COPY requirements.txt root/requirements.txt

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip
RUN apt install -y libglib2.0-dev libpq-dev
RUN pip3 install -r root/requirements.txt


