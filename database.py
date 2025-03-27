import json
from hospital import Appointment, Hospital, Patient, Doctor

class Database:
    @staticmethod
    def save_hospital_data(hospital, filename="hospital_data.json"):
        data = {
            "name": hospital.name,
            "patients": [
                {
                    "name": p.name,
                    "age": p.age,
                    "gender": p.gender,
                    "contact": p.contact,
                    "patient_id": p.patient_id,
                    "medical_history": p.medical_history
                } for p in hospital.patients
            ],
            "doctors": [
                {
                    "name": d.name,
                    "age": d.age,
                    "gender": d.gender,
                    "contact": d.contact,
                    "doctor_id": d.doctor_id,
                    "specialization": d.specialization
                } for d in hospital.doctors
            ],
            "appointments": [
                {
                    "patient_id": a.patient.patient_id,
                    "doctor_id": a.doctor.doctor_id,
                    "date_time": a.date_time,
                    "reason": a.reason,
                    "status": a.status
                } for a in hospital.appointments
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    @staticmethod
    def load_hospital_data(filename="hospital_data.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            hospital = Hospital(data["name"])
            
            # Load patients
            for p_data in data.get("patients", []):
                patient = Patient(
                    p_data["name"],
                    p_data["age"],
                    p_data["gender"],
                    p_data["contact"],
                    p_data["patient_id"],
                    p_data.get("medical_history", [])
                )
                hospital.add_patient(patient)
            
            # Load doctors
            for d_data in data.get("doctors", []):
                doctor = Doctor(
                    d_data["name"],
                    d_data["age"],
                    d_data["gender"],
                    d_data["contact"],
                    d_data["doctor_id"],
                    d_data["specialization"]
                )
                hospital.add_doctor(doctor)
            
            # Load appointments (need to link patient and doctor objects)
            for a_data in data.get("appointments", []):
                patient = hospital.find_patient_by_id(a_data["patient_id"])
                doctor = hospital.find_doctor_by_id(a_data["doctor_id"])
                if patient and doctor:
                    appointment = Appointment(
                        patient,
                        doctor,
                        a_data["date_time"],
                        a_data["reason"]
                    )
                    appointment.status = a_data["status"]
                    hospital.schedule_appointment(appointment)
            
            return hospital
        except FileNotFoundError:
            return Hospital("New Hospital")