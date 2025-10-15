from main import get_weather

def test_get_weather():
    assert get_weather(31) == "hot" ## its some things 'True' or 'False', if its true test case pass else test case fail
    assert get_weather(21) == "cold"
    assert get_weather(41) == "cold"
