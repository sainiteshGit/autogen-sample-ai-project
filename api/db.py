# --- Healthcare MAS Data Structures ---
# Patient vitals database (simulated, keyed by patient_id)
PATIENT_VITALS_DB = {
    "PAT-001": {"age": 72, "heart_rate": 120, "spo2": 85, "history": ["hypertension"]},
    "PAT-002": {"age": 65, "heart_rate": 80, "spo2": 95, "history": ["diabetes"]},
    "PAT-003": {"age": 50, "heart_rate": 75, "spo2": 98, "history": []},
    "PAT-004": {"age": 80, "heart_rate": 130, "spo2": 88, "history": ["COPD"]},
    "PAT-005": {"age": 45, "heart_rate": 70, "spo2": 97, "history": []},
    "PAT-006": {"age": 60, "heart_rate": 110, "spo2": 92, "history": ["asthma"]},
}

# Emergency events log
EMERGENCY_EVENTS_DB = []

# Medication and supplies inventory
MEDICATION_INVENTORY = {
    "epinephrine": 10,
    "aspirin": 20,
    "oxygen": 5,
}

# Insurance/pre-authorization status
INSURANCE_DB = {
    "PAT-001": {"provider": "HealthSecure", "pre_auth": False, "coverage": True},
}
