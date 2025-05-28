# LAIH_DDG_Image_Proxy

FastAPI-сервис для поиска изображений через DuckDuckGo.

## Запуск локально

```bash
pip install -r requirements.txt
uvicorn duckduckgo_image_api:app --host 0.0.0.0 --port 8080
```

## Запуск через Docker

```bash
docker build -t ddg-image-proxy .
docker run -p 8080:8080 ddg-image-proxy
```

## Пример запроса

GET http://localhost:8080/image/search?q=car
