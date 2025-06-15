from db import PATIENT_VITALS_DB, EMERGENCY_EVENTS_DB, MEDICATION_INVENTORY, INSURANCE_DB

# --- Healthcare MAS Tools ---

def monitoring_diagnosis_tool(patient_id: str) -> str:
    """Monitor patient vitals and flag emergencies."""
    patient = PATIENT_VITALS_DB.get(patient_id)
    if not patient:
        return f"Patient {patient_id} not found."
    # Simulate detection logic
    if patient["heart_rate"] > 110 and patient["spo2"] < 90:
        EMERGENCY_EVENTS_DB.append({"patient_id": patient_id, "event": "Possible cardiac arrest"})
        return f"ALERT: Possible cardiac arrest detected for patient {patient_id}. Notify Response Coordination Agent."
    return f"Vitals normal for patient {patient_id}."

def response_coordination_tool(patient_id: str) -> str:
    """Coordinate emergency response for a patient."""
    # Simulate alerting, ICU bed allocation, and transport
    EMERGENCY_EVENTS_DB.append({"patient_id": patient_id, "event": "Response team alerted, ICU bed secured, transport dispatched"})
    return f"Response team alerted, ICU bed secured, and emergency transport dispatched for patient {patient_id}."

def medical_support_tool(patient_id: str) -> str:
    """Prepare medications, supplies, and share patient history."""
    patient = PATIENT_VITALS_DB.get(patient_id)
    if not patient:
        return f"Patient {patient_id} not found."
    # Simulate medication preparation
    meds_prepared = [med for med, qty in MEDICATION_INVENTORY.items() if qty > 0]
    return f"Prepared medications: {', '.join(meds_prepared)}. Shared history: {patient['history']} with doctors."

def administration_billing_tool(patient_id: str) -> str:
    """Contact insurance for emergency approval and coverage."""
    insurance = INSURANCE_DB.get(patient_id)
    if not insurance:
        return f"No insurance record for patient {patient_id}."
    insurance["pre_auth"] = True
    return f"Insurance provider {insurance['provider']} contacted. Emergency approval and coverage confirmed for patient {patient_id}."
