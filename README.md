### Deploy
Для деплоя нужно
- Создать файл с секретами `.env` (можно переименовать и отредактировать `example.env`)
- Собрать образы
```bash
docker compose up --build -d
```
- Зайти в джанго контейнер и сделать миграции
```bash
docker exec -it django19001-v2 bash
python manage.py migrate
```

После этого сайт должен появиться на `localhost:8000/` (порт важен).
