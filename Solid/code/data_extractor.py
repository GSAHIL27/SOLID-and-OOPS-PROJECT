class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_data(self):
        data = []
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        # Skip header and empty lines
        for line in lines[1:]:
            parts = line.split()
            if len(parts) < 3:
                continue
            # Extract Dy, MxT, MnT
            day = parts[0]
            max_temp = int(parts[1])
            min_temp = int(parts[2])
            data.append((day, max_temp, min_temp))
        return data
