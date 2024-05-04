### Секреты
Чувствительные данные собраны в `.env`. Пример - `example.env`.

### Deploy
Для деплоя нужно собрать образы, зайти в джанго контейнер и сделать миграции.
```bash
docker compose up --build -d
docker exec -it django19001-v2 bash
python manage.py migrate
```
