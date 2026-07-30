from ingestion.incident_reader import IncidentReader

reader = IncidentReader()

retorno = reader.read("../data/incidents/incident_001.json")


print(retorno)