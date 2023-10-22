from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from translate import Translator


# Create your views here.


def index(request):
    # ауа сапасының ақпаратын алу
    year = datetime.now().year

    month = datetime.now().strftime("%b")

    day = datetime.now().day

    hour = datetime.now().hour

    minute = datetime.now().minute

    if minute <= 9:
        minute = "0" + str(minute)

    url_aqi = "https://api.waqi.info/feed/A217510/?token=6ed024b9165f16b154982ceca71f3c108a7e6047"

    responce = requests.get(url_aqi)

    json_data = responce.json()

    aqi = json_data["data"]["aqi"]
    pm25 = json_data["data"]["iaqi"]["pm25"]["v"]
    pm10 = json_data["data"]["iaqi"]["pm10"]["v"]

    return render(
        request,
        "index.html",
        {
            "aqi_data": aqi,
            "pm25": pm25,
            "pm10": pm10,
            "minute": minute,
            "hour": hour,
            "day": day,
            "month": month,
            "year": year,
        },
    )


def weather(request):
    # ауа райының ақпаратын алу
    url_weather = "https://api.openweathermap.org/data/2.5/weather?lat=47.1167&lon=51.8833&appid=251257bf514f824f0e370a8d9aa1fa7b&units=metric"

    responce_weather = requests.get(url_weather)

    json_data_weather = responce_weather.json()

    temp_data = json_data_weather["main"]["temp"]
    temp = int(round(temp_data, 0))
    wind = json_data_weather["wind"]["speed"]
    humidity = json_data_weather["main"]["humidity"]
    pressure = (
        str(int(round(((json_data_weather["main"]["pressure"]) * 0.7501), 0)))
        + " мм рт. ст."
    )
    sunrise_data = datetime.fromtimestamp(json_data_weather["sys"]["sunrise"])
    sunrise = sunrise_data.strftime("%H:%M")
    sunset_data = datetime.fromtimestamp(json_data_weather["sys"]["sunset"])
    sunset = sunset_data.strftime("%H:%M")

    description_text = json_data_weather["weather"][0]["description"]
    # ауа райы болжамының ақпаратарын анықтау
    url_forecast = "https://api.openweathermap.org/data/2.5/forecast?lat=47.1167&lon=51.8833&appid=251257bf514f824f0e370a8d9aa1fa7b&units=metric"
    responce_forecast = requests.get(url_forecast)
    json_data_forecast = responce_forecast.json()
    tomorrow_data = datetime.now() + timedelta(days=1)
    tomorrow = tomorrow_data.strftime("%d:%m")

    temp_1 = int(round(json_data_forecast["list"][0]["main"]["temp"], 0))
    wind_1 = int(round(json_data_forecast["list"][0]["wind"]["speed"], 0))
    description_1 = json_data_forecast["list"][0]["weather"][0]["description"]
    pod_1 = json_data_forecast["list"][0]["sys"]["pod"]
    dt_1_data = datetime.fromtimestamp(json_data_forecast["list"][0]["dt"])
    dt_1 = dt_1_data.strftime("%H:%M")

    temp_2 = int(round(json_data_forecast["list"][1]["main"]["temp"], 0))
    wind_2 = int(round(json_data_forecast["list"][1]["wind"]["speed"], 0))
    description_2 = json_data_forecast["list"][1]["weather"][0]["description"]
    pod_2 = json_data_forecast["list"][1]["sys"]["pod"]
    dt_2_data = datetime.fromtimestamp(json_data_forecast["list"][1]["dt"])
    dt_2 = dt_2_data.strftime("%H:%M")

    temp_3 = int(round(json_data_forecast["list"][2]["main"]["temp"], 0))
    wind_3 = int(round(json_data_forecast["list"][2]["wind"]["speed"], 0))
    description_3 = json_data_forecast["list"][2]["weather"][0]["description"]
    pod_3 = json_data_forecast["list"][2]["sys"]["pod"]
    dt_3_data = datetime.fromtimestamp(json_data_forecast["list"][2]["dt"])
    dt_3 = dt_3_data.strftime("%H:%M")

    temp_4 = int(round(json_data_forecast["list"][3]["main"]["temp"], 0))
    wind_4 = int(round(json_data_forecast["list"][3]["wind"]["speed"], 0))
    description_4 = json_data_forecast["list"][3]["weather"][0]["description"]
    pod_4 = json_data_forecast["list"][3]["sys"]["pod"]
    dt_4_data = datetime.fromtimestamp(json_data_forecast["list"][3]["dt"])
    dt_4 = dt_4_data.strftime("%H:%M")

    temp_5 = int(round(json_data_forecast["list"][4]["main"]["temp"], 0))
    wind_5 = int(round(json_data_forecast["list"][4]["wind"]["speed"], 0))
    description_5 = json_data_forecast["list"][4]["weather"][0]["description"]
    pod_5 = json_data_forecast["list"][4]["sys"]["pod"]
    dt_5_data = datetime.fromtimestamp(json_data_forecast["list"][4]["dt"])
    dt_5 = dt_5_data.strftime("%H:%M")

    temp_6 = int(round(json_data_forecast["list"][5]["main"]["temp"], 0))
    wind_6 = int(round(json_data_forecast["list"][5]["wind"]["speed"], 0))
    description_6 = json_data_forecast["list"][5]["weather"][0]["description"]
    pod_6 = json_data_forecast["list"][5]["sys"]["pod"]
    dt_6_data = datetime.fromtimestamp(json_data_forecast["list"][5]["dt"])
    dt_6 = dt_6_data.strftime("%H:%M")

    temp_7 = int(round(json_data_forecast["list"][6]["main"]["temp"], 0))
    wind_7 = int(round(json_data_forecast["list"][6]["wind"]["speed"], 0))
    description_7 = json_data_forecast["list"][6]["weather"][0]["description"]
    pod_7 = json_data_forecast["list"][6]["sys"]["pod"]
    dt_7_data = datetime.fromtimestamp(json_data_forecast["list"][6]["dt"])
    dt_7 = dt_7_data.strftime("%H:%M")

    temp_8 = int(round(json_data_forecast["list"][7]["main"]["temp"], 0))
    wind_8 = int(round(json_data_forecast["list"][7]["wind"]["speed"], 0))
    description_8 = json_data_forecast["list"][7]["weather"][0]["description"]
    pod_8 = json_data_forecast["list"][7]["sys"]["pod"]
    dt_8_data = datetime.fromtimestamp(json_data_forecast["list"][7]["dt"])
    dt_8 = dt_8_data.strftime("%H:%M")

    temp_9 = int(round(json_data_forecast["list"][8]["main"]["temp"], 0))
    wind_9 = int(round(json_data_forecast["list"][8]["wind"]["speed"], 0))
    description_9 = json_data_forecast["list"][8]["weather"][0]["description"]
    pod_9 = json_data_forecast["list"][8]["sys"]["pod"]
    dt_9_data = datetime.fromtimestamp(json_data_forecast["list"][8]["dt"])
    dt_9 = dt_9_data.strftime("%H:%M")

    temp_10 = int(round(json_data_forecast["list"][9]["main"]["temp"], 0))
    wind_10 = int(round(json_data_forecast["list"][9]["wind"]["speed"], 0))
    description_10 = json_data_forecast["list"][9]["weather"][0]["description"]
    pod_10 = json_data_forecast["list"][9]["sys"]["pod"]
    dt_10_data = datetime.fromtimestamp(json_data_forecast["list"][9]["dt"])
    dt_10 = dt_10_data.strftime("%H:%M")

    temp_11 = int(round(json_data_forecast["list"][10]["main"]["temp"], 0))
    wind_11 = int(round(json_data_forecast["list"][10]["wind"]["speed"], 0))
    description_11 = json_data_forecast["list"][10]["weather"][0]["description"]
    pod_11 = json_data_forecast["list"][10]["sys"]["pod"]
    dt_11_data = datetime.fromtimestamp(json_data_forecast["list"][10]["dt"])
    dt_11 = dt_11_data.strftime("%H:%M")

    temp_12 = int(round(json_data_forecast["list"][11]["main"]["temp"], 0))
    wind_12 = int(round(json_data_forecast["list"][11]["wind"]["speed"], 0))
    description_12 = json_data_forecast["list"][11]["weather"][0]["description"]
    pod_12 = json_data_forecast["list"][11]["sys"]["pod"]
    dt_12_data = datetime.fromtimestamp(json_data_forecast["list"][11]["dt"])
    dt_12 = dt_12_data.strftime("%H:%M")

    temp_13 = int(round(json_data_forecast["list"][12]["main"]["temp"], 0))
    wind_13 = int(round(json_data_forecast["list"][12]["wind"]["speed"], 0))
    description_13 = json_data_forecast["list"][12]["weather"][0]["description"]
    pod_13 = json_data_forecast["list"][12]["sys"]["pod"]
    dt_13_data = datetime.fromtimestamp(json_data_forecast["list"][12]["dt"])
    dt_13 = dt_13_data.strftime("%H:%M")

    temp_14 = int(round(json_data_forecast["list"][13]["main"]["temp"], 0))
    wind_14 = int(round(json_data_forecast["list"][13]["wind"]["speed"], 0))
    description_14 = json_data_forecast["list"][13]["weather"][0]["description"]
    pod_14 = json_data_forecast["list"][13]["sys"]["pod"]
    dt_14_data = datetime.fromtimestamp(json_data_forecast["list"][13]["dt"])
    dt_14 = dt_14_data.strftime("%H:%M")

    temp_15 = int(round(json_data_forecast["list"][14]["main"]["temp"], 0))
    wind_15 = int(round(json_data_forecast["list"][14]["wind"]["speed"], 0))
    description_15 = json_data_forecast["list"][14]["weather"][0]["description"]
    pod_15 = json_data_forecast["list"][14]["sys"]["pod"]
    dt_15_data = datetime.fromtimestamp(json_data_forecast["list"][14]["dt"])
    dt_15 = dt_15_data.strftime("%H:%M")

    temp_16 = int(round(json_data_forecast["list"][15]["main"]["temp"], 0))
    wind_16 = int(round(json_data_forecast["list"][15]["wind"]["speed"], 0))
    description_16 = json_data_forecast["list"][15]["weather"][0]["description"]
    pod_16 = json_data_forecast["list"][15]["sys"]["pod"]
    dt_16_data = datetime.fromtimestamp(json_data_forecast["list"][15]["dt"])
    dt_16 = dt_16_data.strftime("%H:%M")

    temp_17 = int(round(json_data_forecast["list"][16]["main"]["temp"], 0))
    wind_17 = int(round(json_data_forecast["list"][16]["wind"]["speed"], 0))
    description_17 = json_data_forecast["list"][16]["weather"][0]["description"]
    pod_17 = json_data_forecast["list"][16]["sys"]["pod"]
    dt_17_data = datetime.fromtimestamp(json_data_forecast["list"][16]["dt"])
    dt_17 = dt_17_data.strftime("%H:%M")

    temp_18 = int(round(json_data_forecast["list"][17]["main"]["temp"], 0))
    wind_18 = int(round(json_data_forecast["list"][17]["wind"]["speed"], 0))
    description_18 = json_data_forecast["list"][17]["weather"][0]["description"]
    pod_18 = json_data_forecast["list"][17]["sys"]["pod"]
    dt_18_data = datetime.fromtimestamp(json_data_forecast["list"][17]["dt"])
    dt_18 = dt_18_data.strftime("%H:%M")

    # ауа райының сипаттамасын қазақ тіліне аудару
    translator = Translator(from_lang="english", to_lang="kazakh")

    text_Rus = translator.translate(description_text)
    if "weather condition" in text_Rus:
        text = text_Rus.replace("weather condition", "")
    else:
        text = text_Rus.replace("weather forecast", "")

    description = text.capitalize()
    if description_text == "few clouds":
        description = "Айнымалы бұлттар"
    if description_text == "broken clouds":
        description = "Жыртылған бұлттар"
    if description_text == "shower rain":
        description = "Қатты жаңбыр"
    if description_text == "thunderstorm":
        description = "Найзағай"

    # ауа райына + немесе - белгілерін қою
    if temp < 0:
        temp_data = "-" + str(temp)

    else:
        temp_data = "+" + str(temp)

    return render(
        request,
        "weather.html",
        {
            "temp": temp_data,
            "wind": wind,
            "humidity": humidity,
            "pressure": pressure,
            "description": description,
            "sunrise": sunrise,
            "sunset": sunset,
            "tomorrow": tomorrow,
            "temp_1": temp_1,
            "wind_1": temp_1,
            "description_1": description_1,
            "pod_1": pod_1,
            "dt_1": dt_1,
            "temp_2": temp_2,
            "wind_2": temp_2,
            "description_2": description_2,
            "pod_2": pod_2,
            "dt_2": dt_2,
            "temp_3": temp_3,
            "wind_3": temp_3,
            "description_3": description_3,
            "pod_3": pod_3,
            "dt_3": dt_3,
            "temp_4": temp_4,
            "wind_4": temp_4,
            "description_4": description_4,
            "pod_4": pod_4,
            "dt_4": dt_4,
            "temp_5": temp_5,
            "wind_5": temp_5,
            "description_5": description_5,
            "pod_5": pod_5,
            "dt_5": dt_5,
            "temp_6": temp_6,
            "wind_6": temp_6,
            "description_6": description_6,
            "pod_6": pod_6,
            "dt_6": dt_6,
            "temp_7": temp_7,
            "wind_7": temp_7,
            "description_7": description_7,
            "pod_7": pod_7,
            "dt_7": dt_7,
            "temp_8": temp_8,
            "wind_8": temp_8,
            "description_8": description_8,
            "pod_8": pod_8,
            "dt_8": dt_8,
            "temp_9": temp_9,
            "wind_9": temp_9,
            "description_9": description_9,
            "pod_9": pod_9,
            "dt_9": dt_9,
            "temp_10": temp_10,
            "wind_10": temp_10,
            "description_10": description_10,
            "pod_10": pod_10,
            "dt_10": dt_10,
            "temp_11": temp_11,
            "wind_11": temp_11,
            "description_11": description_11,
            "pod_11": pod_11,
            "dt_11": dt_11,
            "temp_12": temp_12,
            "wind_12": temp_12,
            "description_12": description_12,
            "pod_12": pod_12,
            "dt_12": dt_1,
            "temp_13": temp_13,
            "wind_13": temp_13,
            "description_13": description_13,
            "pod_13": pod_13,
            "dt_13": dt_13,
            "temp_14": temp_14,
            "wind_14": temp_14,
            "description_14": description_14,
            "pod_14": pod_14,
            "dt_14": dt_14,
            "temp_15": temp_15,
            "wind_15": temp_15,
            "description_15": description_15,
            "pod_15": pod_15,
            "dt_15": dt_15,
            "temp_16": temp_16,
            "wind_16": temp_16,
            "description_16": description_16,
            "pod_16": pod_16,
            "dt_16": dt_16,
        },
    )
