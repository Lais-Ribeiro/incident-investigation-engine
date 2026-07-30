import json

class IncidentReader:
    def read(self, file_path):
        with open(file_path, "r") as file:
            incident = json.load(file)
        return incident
