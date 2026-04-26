# Contact class (base class)
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# EmergencyContact inherits from Contact
class EmergencyContact(Contact):
    def __init__(self, name, phone):
        super().__init__(name, phone)

# InsuranceInfo class for multiple inheritance
class InsuranceInfo:
    def __init__(self, provider, policy_number):
        self.provider = provider
        self.policy_number = policy_number

# Patient class
class Patient:
    def __init__(self, first, middle, last, address, city, state, zip_code, phone, emergency_contact):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_contact = emergency_contact

# Multiple inheritance
class InsuredPatient(Patient, InsuranceInfo):
    def __init__(self, first, middle, last, address, city, state, zip_code, phone, emergency_contact,
                 provider, policy_number):
        Patient.__init__(self, first, middle, last, address, city, state, zip_code, phone, emergency_contact)
        InsuranceInfo.__init__(self, provider, policy_number)

# VIPPatient class (inherits from Patient)
class VIPPatient(Patient):
    def __init__(self, first, middle, last, address, city, state, zip_code, phone, emergency_contact, vip_level):
        super().__init__(first, middle, last, address, city, state, zip_code, phone, emergency_contact)
        self.vip_level = vip_level
        self.total_charges = 0

    # New method
    def apply_discount(self, percent):
        discount_amount = self.total_charges * (percent / 100)
        self.total_charges -= discount_amount
        return discount_amount

    # Override method
    def display_info(self):
        print("VIP PATIENT INFORMATION")
        print("-----------------------")
        print(f"Name: {self.first} {self.middle} {self.last}")
        print(f"VIP Level: {self.vip_level}")
        print(f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}")
        print(f"Phone #: {self.phone}")
        print(f"Emergency Contact: {self.emergency_contact.name} ({self.emergency_contact.phone})")
        print(f"Current Charges: ${self.total_charges:.2f}")

# Procedure class
class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

# Emergency contact object
em_contact = EmergencyContact("Pawel Brzozka", "8473872736")
# Patient object
patient = Patient(
    "Michael", "J.", "Brzozka", "123 Main St", "Rolling Meadows", "IL", "60008", "3123751506",
    em_contact
)
# Procedure objects
p1 = Procedure("Physical Exam", "04.18.2026", "Dr. Irvine", 250.00)
p2 = Procedure("X-ray", "04.18.2026", "Dr. Jamison", 500.00)
p3 = Procedure("Blood Test", "04.18.2026", "Dr. Smith", 200.00)
# # Display patient info
# print("PATIENT INFORMATION")
# print("-------------------")
# print("Name:", patient.first, patient.middle, patient.last)
# print("Address:", patient.address)
# print("City/State/ZIP:", patient.city, patient.state, patient.zip_code)
# print("Phone #:", patient.phone)
# print("Emergency Contact:", patient.emergency_contact.name, patient.emergency_contact.phone)
# print()
# # Display procedures
# print("PROCEDURES")
# print("----------")
# for proc in [p1, p2, p3]:
#     print("Procedure:", proc.name)
#     print("Date:", proc.date)
#     print("Practitioner:", proc.practitioner)
#     print("Charge: $", proc.charge)
#     print()
# # Total charges
# total = p1.charge + p2.charge + p3.charge
# print("Total Charges: $", total)

# Demonstration
print("~~~~~ VIP PATIENT DEMONSTRATION ~~~~~")
vip_contact = EmergencyContact("Grace Brzozka", "8473126913")
vip = VIPPatient(
    "Thomas", "J.", "Brzozka",
    "123 Main St", "Rolling Meadows", "IL", "60008",
    "8479258265",
    vip_contact,
    vip_level="Gold"
)
# Add charges
vip.total_charges = 1000.00
print("\n--- BEFORE DISCOUNT ---")
vip.display_info()
# Apply discount
discount = vip.apply_discount(15)
print("\n--- AFTER 15% DISCOUNT ---")
vip.display_info()
print(f"Discount Applied: ${discount:.2f}")
