class WeatherAnalyzer:
    def find_min_diff(self, data):
        min_diff = float('inf')
        min_day = None
        for day, max_temp, min_temp in data:
            diff = abs(max_temp - min_temp)
            if diff < min_diff:
                min_diff = diff
                min_day = day
        return min_day


class SoccerAnalyzer:
    def find_min_diff(self, data):
        min_diff = float('inf')
        min_team = None
        for team, for_goals, against_goals in data:
            diff = abs(for_goals - against_goals)
            if diff < min_diff:
                min_diff = diff
                min_team = team
        return min_team
