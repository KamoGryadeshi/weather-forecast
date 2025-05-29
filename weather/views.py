import requests
from django.shortcuts import render
from django.http import JsonResponse

def autocomplete(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        try:
            geo_url = f'https://geocoding-api.open-meteo.com/v1/search?name={query}&count=5'
            response = requests.get(geo_url).json()
            for place in response.get('results', []):
                name = place['name']
                country = place['country']
                results.append(f"{name}, {country}")
        except Exception as e:
            print(f"Error in autocomplete: {e}")

    return JsonResponse(results, safe=False)

def home(request):
    weather_data = None
    error = None
    last_city = request.COOKIES.get('last_city')

    if 'city' in request.GET:
        city = request.GET['city']
        geo_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1'

        try:
            geo_response = requests.get(geo_url).json()
            if geo_response.get("results"):
                lat = geo_response['results'][0]['latitude']
                lon = geo_response['results'][0]['longitude']

                weather_url = (
                    f'https://api.open-meteo.com/v1/forecast'
                    f'?latitude={lat}&longitude={lon}&current_weather=true'
                )
                weather_response = requests.get(weather_url).json()
                weather_data = weather_response.get('current_weather', {})

                # Устанавливаем куку с последним городом
                response = render(request, 'weather/home.html', {
                    'weather': weather_data,
                    'error': error,
                    'last_city': city  # передаём, чтобы показать сразу
                })
                response.set_cookie('last_city', city, max_age=60*60*24*30)  # 30 дней
                return response

            else:
                error = 'Город не найден.'

        except Exception as e:
            error = f'Ошибка при получении данных: {e}'

    return render(request, 'weather/home.html', {
        'weather': weather_data,
        'error': error,
        'last_city': last_city
    })

