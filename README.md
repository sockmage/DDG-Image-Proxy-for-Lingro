# LAIH_DDG_Image_Proxy

FastAPI-сервис для поиска изображений через DuckDuckGo. Используется в связке с Language AI Helper для поиска и отправки изображений пользователям.

## Особенности

- Поиск изображений через DuckDuckGo (без ключей и ограничений Unsplash)
- Легко деплоится на Railway, Render, VPS, Docker и др.
- Простое API: GET /image/search?q=...

## Запуск

### Локально

```bash
pip install -r requirements.txt
uvicorn duckduckgo_image_api:app --host 0.0.0.0 --port 8080
```

### Через Docker

```bash
docker build -t ddg-image-proxy .
docker run -p 8080:8080 ddg-image-proxy
```

## Пример запроса

```
GET http://localhost:8080/image/search?q=car
```

## Деплой на Railway
1. Зайдите на [Railway](https://railway.app/), создайте новый проект.
2. Подключите репозиторий с LAIH_DDG_Image_Proxy.
3. Railway автоматически определит Python и запустит сервис.

## Лицензия

GPL-2.0
