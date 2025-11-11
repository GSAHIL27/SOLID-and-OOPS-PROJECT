from data_extractor import DataExtractor
from data_analyzer import WeatherAnalyzer, SoccerAnalyzer

class Calculator:
    def __init__(self, file_path, analyzer_type):
        self.file_path = file_path
        self.extractor = DataExtractor(file_path)
        self.analyzer = analyzer_type()

    def execute(self):
        data = self.extractor.extract_data()
        return self.analyzer.find_min_diff(data)
