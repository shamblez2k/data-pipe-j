# db-updater

helloworld for db-updater app

# Spin up locally

cd src
uvicorn main:app --reload

# In a separate terminal

sudo docker run -d -p 127.0.0.1:3306:3306 gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.13.0 -address 0.0.0.0 --port 3306

# In Web browser

http://127.0.0.1:8000/docs#
