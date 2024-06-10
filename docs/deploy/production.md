**Для кого:** разработчики / админы

**Что:** инструкция как развернуть сайт на прод-сервере

---

Деплой на прод от локального отличается сертификатами и nginx-ом.

Последовательность действий:

- Создать файл с секретами `.env`. Подробно - [тут](/docs/deploy/secrets.md)
- Создать nginx-конфиг в `nginx.conf`
- В `data/certbot` положить сертификаты
- Поднять докер-контейнер
```bash
docker compose --profile prod up -d
```
- Выплнить Django-миграции
```bash
docker exec -it django19001-v2 python manage.py migrate
```

После этого сайт должен появиться на [https://avarus.space/](https://avarus.space/) (порт важен).
