# Activity Health ML App

A Flask-based application that evaluates a user's daily activity level and assigns a health grade.

## Features

- Activity score calculation
- Grade classification (A–D)
- Health recommendations
- Flask web interface
- REST API endpoints
- Docker containerization

## Run with Docker

docker build -t activity-app .
docker run -p 5000:5000 activity-app
