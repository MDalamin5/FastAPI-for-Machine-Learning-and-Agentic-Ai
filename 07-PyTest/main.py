def get_weather(temp: int) -> str:
    if temp > 20:
        return "cold"
    else:
        return "hot"