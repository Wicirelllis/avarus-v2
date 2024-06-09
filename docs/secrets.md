Этот файл содержит подробное описание `.env`-файла с секретами.
`.env` содержит чувствительную информацию (пароли, почты, итд), поэтому не должен публиковаться.

Пример заполнения - [тут](/example.env)

Для обозначения строк нужно использовать двойные кавычки - "".

#

### django
Общие django-настройки.

`SECRET_KEY`: `str` - секретный ключ Django. Используется, например, для  соления паролей.

`EMAIL_HOST_USER`: `str` - email с которого будут отправляться пиьма с оповещениями

`EMAIL_HOST_PASSWORD`: `str` - пароль (или токен) от адреса выше

`YANDEX_MAPS_API_TOKEN`: `str` - ключ от API Яндекс.Карт (JavaScript API и HTTP Геокодер)

### postgress
`POSTGRES_USER`: `str` - пользователь БД

`POSTGRES_PASSWORD`: `str` - пароль от БД

`POSTGRES_DB`: `str` - название БД

### feedback
На странице `About us` есть форма фибека.
Весь фидбек сохраняется в БД, но можно еще отправлять email при создании фидбека.

`FEEDBACK_SEND_EMAIL`: `bool` - Отправлять ли письмо

`FEEDBACK_EMAIL_RECIPIENTS`: `list[str]` - список адресатов, кому отправлять письмо с фидбеком.
Если адрес только один, то список из одного элемента.

### dataset access request
После регистрации пользователь может заполнить форму и запросить доступ к приватному датасету.
Этот запрос сохраняется в БД, но можно также отправлять письмо.
Вполне аналогичтно фидбеку.
Обратите внимание, что это отдельные, независимые настройки.

`DATASET_REQUEST_SEND_EMAIL`: `bool` - Отправлять ли письмо

`DATASET_REQUEST_EMAIL_RECIPIENTS`: `list[str]` - список адресатов, кому отправлять письмо о запросе доступа к датасету

#

### Как получить токен для gmail
При использовании gmail использовать пароль не получится из-за 2FA, поэтому нужно создать токен.

- Зайти на `https://myaccount.google.com/apppasswords`
- Заполнить название и создать новый пароль для приложения
- Сохранить его в `EMAIL_HOST_PASSWORD`

### Как получить токен для Яндекс.Карт
Для отрисовки карты на главной сайта нужно получить токен API Яндекс.Карт.
Делается в кабинете разработчика.

- В кабинете разработчика (developer.tech.yandex.ru/services)
- Родключить `JavaScript API и HTTP Геокодер`
- В нем создать новый ключ
- Сохранить ключ в `YANDEX_MAPS_API_TOKEN`