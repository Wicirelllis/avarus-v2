#!/bin/bash
docker compose up --build -d
sleep 10
docker exec -it django19001-v2 python manage.py migrate
