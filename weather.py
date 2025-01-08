import tkinter as tk
from tkinter import messagebox
import requests
import json

# Function to fetch the weather
def get_weather():
    city = city_entry.get()
    api_key = "df5b9ea81a21a805f4949b1b064ccd8d"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            # Extracting data from the response
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            description = weather["description"]

            # Updating the UI with weather details
            temperature_label.config(text=f"Temperature: {temperature}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            description_label.config(text=f"Description: {description.capitalize()}")

        else:
            messagebox.showerror("Error", "City not found or invalid API key")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch data. Check your internet connection.")

# Create the main window
root = tk.Tk()
root.title("Live Weather Desktop")

# Create and place widgets
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

temperature_label = tk.Label(root, text="Temperature: N/A")
temperature_label.pack(pady=5)

humidity_label = tk.Label(root, text="Humidity: N/A")
humidity_label.pack(pady=5)

description_label = tk.Label(root, text="Description: N/A")
description_label.pack(pady=5)

# Run the application
root.mainloop()