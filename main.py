import tkinter as tk
import urllib.request
import json


API_KEY = '1997b6990880ff8d697ac301365c6673'


def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))

        if data['cod'] == 200:
            # Extract weather data
            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            result_label.config(
                text=f'Temperature: {temperature}°C\nDescription: {description}',
                fg="green",
                bg="#F0F0F0"
            )
        else:
            result_label.config(
                text='City not found',
                fg="red",
                bg="#F0F0F0"
            )
    except Exception as e:
        result_label.config(
            text='An error occurred',
            fg="red",
            bg="#F0F0F0"
        )


window = tk.Tk()
window.title("Weather App")
window.geometry("400x200")


title_label = tk.Label(window, text="Weather App", font=(
    "Helvetica", 20), bg="#3498db", fg="white")
title_label.pack(fill="x")

city_label = tk.Label(window, text="Enter City:",
                      font=("Helvetica", 12), bg="#F0F0F0")
city_label.pack()

city_entry = tk.Entry(window, font=("Helvetica", 12))
city_entry.pack(pady=10)

get_weather_button = tk.Button(window, text="Get Weather", command=lambda: get_weather(
    city_entry.get()), font=("Helvetica", 12), bg="#2ecc71", fg="white")
get_weather_button.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#F0F0F0")
result_label.pack(pady=10, fill="both", expand=True)

window.mainloop()
