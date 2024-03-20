import queue

class DeskManagerSystem:
    def __init__(self):
        self.patient_queue = queue.Queue()

    def register_patient(self, patient_name):
        self.patient_queue.put(patient_name)
        print(f"Patient '{patient_name}' registered.")

    def remove_patient(self):
        if not self.patient_queue.empty():
            patient_name = self.patient_queue.get()
            print(f"Patient '{patient_name}' has met the doctor and is now removed from the queue.")
        else:
            print("There are no patients in the queue.")

    def display_patient_queue(self):
        if self.patient_queue.empty():
            print("The patient queue is currently empty.")
        else:
            print("Current patient queue:")
            for index, patient in enumerate(list(self.patient_queue.queue), start=1):
                print(f"{index}. {patient}")

def main():
    system = DeskManagerSystem()
    while True:
        print("\nDesk Manager System")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            patient_name = input("Enter patient name to register: ")
            system.register_patient(patient_name)

        elif choice == "2":
            system.remove_patient()

        elif choice == "3":
            system.display_patient_queue()

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
