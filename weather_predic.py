def predict_weather(temperature, humidity):
    """
    Predict weather based on temperature (°C) and humidity (%)
    """
    if temperature > 30 and humidity < 50:
        return "Sunny"
    elif temperature > 25 and humidity >= 50:
        return "Cloudy"
    elif temperature <= 25 and humidity > 70:
        return "Rainy"
    elif temperature <= 0:
        return "Snowy"
    else:
        return "Windy"

# Example usage
temp = float(input("Enter temperature (°C): "))
hum = float(input("Enter humidity (%): "))

weather = predict_weather(temp, hum)
print(f"Predicted Weather: {weather}")
