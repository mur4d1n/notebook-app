# notebook-app

Миниатюрный бэкенд для приложения-ежедневника, реализующий самую базовую функциональность.

Запуск приложения осуществляется с помощью Docker Compose:

```shell
docker-compose up -d
```

Приложение предоставляет простейшее API для взаимодействия с СУБД, где хранятся наши заметки. Доступ к API осуществляется по локалхосту на порту `8080`. 

Подробная информация по эндпоинтам доступна по адресу `127.0.0.1:8080/docs` или `127.0.0.1:8080/redoc`.
