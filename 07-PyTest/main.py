def get_weather(temp: int) -> str:
    if temp > 30:
        return "hot"
    else:
        return "cold"