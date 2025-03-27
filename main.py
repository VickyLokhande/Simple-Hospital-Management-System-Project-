from hospital import Hospital, Patient, Doctor, Appointment
from database import Database

def main():
    # Load hospital data from file
    hospital = Database.load_hospital_data()
    
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Add Medical Record")
        print("8. Complete Appointment")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Add Patient
            print("\nAdd New Patient")
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            contact = input("Contact: ")
            patient_id = input("Patient ID: ")
            
            patient = Patient(name, age, gender, contact, patient_id)
            hospital.add_patient(patient)
            Database.save_hospital_data(hospital)
            print("Patient added successfully!")
        
        elif choice == "2":
            # Add Doctor
            print("\nAdd New Doctor")
            name = input("Name: ")
            age = input("Age: ")
            gender = input("Gender: ")
            contact = input("Contact: ")
            doctor_id = input("Doctor ID: ")
            specialization = input("Specialization: ")
            
            doctor = Doctor(name, age, gender, contact, doctor_id, specialization)
            hospital.add_doctor(doctor)
            Database.save_hospital_data(hospital)
            print("Doctor added successfully!")
        
        elif choice == "3":
            # Schedule Appointment
            print("\nSchedule Appointment")
            patient_id = input("Patient ID: ")
            doctor_id = input("Doctor ID: ")
            date_time = input("Date/Time (YYYY-MM-DD HH:MM): ")
            reason = input("Reason: ")
            
            patient = hospital.find_patient_by_id(patient_id)
            doctor = hospital.find_doctor_by_id(doctor_id)
            
            if patient and doctor:
                appointment = Appointment(patient, doctor, date_time, reason)
                hospital.schedule_appointment(appointment)
                Database.save_hospital_data(hospital)
                print("Appointment scheduled successfully!")
            else:
                print("Patient or Doctor not found!")
        
        elif choice == "4":
            # View Patients
            print("\nPatient List")
            hospital.display_patients()
        
        elif choice == "5":
            # View Doctors
            print("\nDoctor List")
            hospital.display_doctors()
        
        elif choice == "6":
            # View Appointments
            print("\nAppointment List")
            hospital.display_appointments()
        
        elif choice == "7":
            # Add Medical Record
            print("\nAdd Medical Record")
            patient_id = input("Patient ID: ")
            patient = hospital.find_patient_by_id(patient_id)
            
            if patient:
                diagnosis = input("Diagnosis: ")
                treatment = input("Treatment: ")
                doctor_id = input("Doctor ID: ")
                doctor = hospital.find_doctor_by_id(doctor_id)
                
                if doctor:
                    patient.add_medical_record(diagnosis, treatment, doctor)
                    Database.save_hospital_data(hospital)
                    print("Medical record added successfully!")
                else:
                    print("Doctor not found!")
            else:
                print("Patient not found!")
        
        elif choice == "8":
            # Complete Appointment
            print("\nComplete Appointment")
            patient_id = input("Patient ID: ")
            appointments = hospital.get_patient_appointments(patient_id)
            
            if appointments:
                for i, appt in enumerate(appointments, 1):
                    print(f"{i}. {appt.date_time} - {appt.reason} ({appt.status})")
                
                appt_choice = int(input("Select appointment to complete: ")) - 1
                if 0 <= appt_choice < len(appointments):
                    appointments[appt_choice].complete_appointment()
                    Database.save_hospital_data(hospital)
                    print("Appointment marked as completed!")
                else:
                    print("Invalid selection!")
            else:
                print("No appointments found for this patient!")
        
        elif choice == "9":
            # Exit
            print("Exiting Hospital Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()