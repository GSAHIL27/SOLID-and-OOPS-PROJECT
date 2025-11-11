from calculator import Calculator
from data_analyzer import SoccerAnalyzer

data_path = "../data/football.dat"

soccer_calculator = Calculator(file_path=data_path, analyzer_type=SoccerAnalyzer)
result = soccer_calculator.execute()

print("Team with smallest goal difference:", result)
