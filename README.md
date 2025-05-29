
# Weather Forecast App

Веб-приложение, где пользователь может ввести название города и получить прогноз погоды.

## Использованные технологии:

- Python 3.x
- Django 4.x
- HTML, JavaScript (fetch API для автозаполнения)
- [Open-Meteo API](https://open-meteo.com/)
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)

---

## Запуск

1. Клонируйте репозиторий:
2. Создайте и активируйте виртуальное окружение:
3. Установите зависимости:
4. Запустите сервер:
```bash
python manage.py runserver
```
5. Перейдите в браузере по адресу:
```
http://127.0.0.1:8000/
```


## Что реализовано:

-  Получение прогноза погоды по введённому городу
-  Использование Open-Meteo API
-  Автодополнение при вводе города
-  При повторном посещении — предложение посмотреть погоду в ранее введённом городе

---


## Структура проекта

```
weather_project/
├── weather/
│   ├── templates/
│   │   └── weather/
│   │       └── home.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── weather_project/
│   └── settings.py
├── manage.py
└── requirements.txt
```

