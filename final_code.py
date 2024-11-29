import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv("year_lahore_weather_data.csv")

# Convert 'Date' to datetime for proper handling
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Plot temperature trends
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Min_Temperature'], label="Min Temperature (°C)", color="blue")
plt.plot(weather_data['Date'], weather_data['Max_Temperature'], label="Max Temperature (°C)", color="red")
plt.title("Temperature Trends Over the Year (Lahore)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()

# Plot humidity trends
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Humidity'], label="Humidity (%)", color="green")
plt.title("Humidity Trends Over the Year (Lahore)")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.legend()
plt.grid(True)
plt.show()

# Plot wind speed trends
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Wind_Speed'], label="Wind Speed (units)", color="orange")
plt.title("Wind Speed Trends Over the Year (Lahore)")
plt.xlabel("Date")
plt.ylabel("Wind Speed (units)")
plt.legend()
plt.grid(True)
plt.show()

# Combined visualization
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Min_Temperature'], label="Min Temperature (°C)", color="blue", alpha=0.7)
plt.plot(weather_data['Date'], weather_data['Max_Temperature'], label="Max Temperature (°C)", color="red", alpha=0.7)
plt.plot(weather_data['Date'], weather_data['Humidity'], label="Humidity (%)", color="green", alpha=0.7)
plt.plot(weather_data['Date'], weather_data['Wind_Speed'], label="Wind Speed (units)", color="orange", alpha=0.7)
plt.title("Weather Trends Over the Year (Lahore)")
plt.xlabel("Date")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()
