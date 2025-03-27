import json
from datetime import datetime

class Person:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

class Patient(Person):
    def __init__(self, name, age, gender, contact, patient_id, medical_history=None):
        super().__init__(name, age, gender, contact)
        self.patient_id = patient_id
        self.medical_history = medical_history or []
    
    def add_medical_record(self, diagnosis, treatment, doctor):
        record = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'diagnosis': diagnosis,
            'treatment': treatment,
            'doctor': doctor.name
        }
        self.medical_history.append(record)
    
    def __str__(self):
        return f"Patient ID: {self.patient_id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nContact: {self.contact}"

class Doctor(Person):
    def __init__(self, name, age, gender, contact, doctor_id, specialization):
        super().__init__(name, age, gender, contact)
        self.doctor_id = doctor_id
        self.specialization = specialization
    
    def __str__(self):
        return f"Doctor ID: {self.doctor_id}\nName: {self.name}\nSpecialization: {self.specialization}\nContact: {self.contact}"

class Appointment:
    def __init__(self, patient, doctor, date_time, reason):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
        self.reason = reason
        self.status = "Scheduled"  # Can be: Scheduled, Completed, Cancelled
    
    def complete_appointment(self):
        self.status = "Completed"
    
    def cancel_appointment(self):
        self.status = "Cancelled"
    
    def __str__(self):
        return f"Appointment:\nPatient: {self.patient.name}\nDoctor: {self.doctor.name}\nDate/Time: {self.date_time}\nReason: {self.reason}\nStatus: {self.status}"

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []
    
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
    
    def find_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None
    
    def find_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None
    
    def get_patient_appointments(self, patient_id):
        return [appt for appt in self.appointments if appt.patient.patient_id == patient_id]
    
    def get_doctor_appointments(self, doctor_id):
        return [appt for appt in self.appointments if appt.doctor.doctor_id == doctor_id]
    
    def display_patients(self):
        for patient in self.patients:
            print(patient)
            print("-" * 30)
    
    def display_doctors(self):
        for doctor in self.doctors:
            print(doctor)
            print("-" * 30)
    
    def display_appointments(self):
        for appointment in self.appointments:
            print(appointment)
            print("-" * 30)