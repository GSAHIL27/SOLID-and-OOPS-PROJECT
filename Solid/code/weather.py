from calculator import Calculator
from data_analyzer import WeatherAnalyzer

data_path = "../data/weather.dat"

weather_calculator = Calculator(file_path=data_path, analyzer_type=WeatherAnalyzer)
result = weather_calculator.execute()

print("Day with smallest temperature spread:", result)
