# Hospital Appointment Management System
appointments = []

def book_appointment():
    print("\n--- Book Appointment ---")

    patient_name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    doctor = input("Enter doctor name: ")
    date = input("Enter appointment date (DD-MM-YYYY): ")
    time = input("Enter appointment time: ")

    appointment = {
        "Patient": patient_name,
        "Age": age,
        "Doctor": doctor,
        "Date": date,
        "Time": time
    }

    appointments.append(appointment)

    print("\nAppointment booked successfully!")


def view_appointments():
    print("\n--- Appointment List ---")

    if len(appointments) == 0:
        print("No appointments available.")
    else:
        for i, appointment in enumerate(appointments, start=1):
            print("\nAppointment", i)
            print("Patient Name :", appointment["Patient"])
            print("Age          :", appointment["Age"])
            print("Doctor       :", appointment["Doctor"])
            print("Date         :", appointment["Date"])
            print("Time         :", appointment["Time"])


def cancel_appointment():
    print("\n--- Cancel Appointment ---")

    if len(appointments) == 0:
        print("No appointments available.")
        return

    for i, appointment in enumerate(appointments, start=1):
        print(i, "-", appointment["Patient"],
              "-", appointment["Date"])

    number = int(input("Enter appointment number to cancel: "))

    if 1 <= number <= len(appointments):
        appointments.pop(number - 1)
        print("Appointment cancelled successfully!")
    else:
        print("Invalid appointment number.")


while True:

    print("\n===================================")
    print(" HOSPITAL APPOINTMENT MANAGEMENT")
    print("===================================")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_appointment()

    elif choice == "2":
        view_appointments()

    elif choice == "3":
        cancel_appointment()

    elif choice == "4":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice. Please try again.")