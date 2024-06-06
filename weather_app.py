import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecasting App")
        
        # Frame for the city input
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        
        # Label and entry widget for city name
        self.city_label = tk.Label(self.input_frame, text="City:", font=("Helvetica", 12))
        self.city_label.pack(side=tk.LEFT, padx=5)
        
        self.city_entry = tk.Entry(self.input_frame, font=("Helvetica", 12))
        self.city_entry.pack(side=tk.LEFT, padx=5)
        
        # Button to get weather
        self.get_weather_button = tk.Button(self.input_frame, text="Get Weather", font=("Helvetica", 12), command=self.get_weather)
        self.get_weather_button.pack(side=tk.LEFT, padx=5)
        
        # Frame for displaying weather
        self.weather_frame = tk.Frame(self.root)
        self.weather_frame.pack(pady=10)
        
        # Label to display weather
        self.weather_label = tk.Label(self.weather_frame, text="", font=("Helvetica", 12))
        self.weather_label.pack()
    
    def get_weather(self):
        city = self.city_entry.get()
        if city:
            api_key = "6a7d8ba4642ea0b387bf0f616e90fcc3"  # Replace with your actual API key
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
            
            response = requests.get(complete_url)
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                weather = data['weather'][0]
                
                temp = main['temp']
                humidity = main['humidity']
                description = weather['description']
                
                weather_info = f"Temperature: {temp}°C\nHumidity: {humidity}%\nDescription: {description.capitalize()}"
                self.weather_label.config(text=weather_info)
            else:
                messagebox.showerror("Error", "City not found. Please enter a valid city name.")
        else:
            messagebox.showwarning("Warning", "You must enter a city name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
