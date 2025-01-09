from django.db import models

# Address Model
class Address(models.Model):
    line_1 = models.CharField(max_length=255)
    line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.line_1}, {self.city}, {self.state}"

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Employee Model
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Patient Model
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Appointment Model
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, limit_choices_to={'role__name': 'Doctor'})
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"

# Prescription Model
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=50)
    instructions = models.TextField()

# MedicalRecord Model
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateField()
    description = models.TextField()
    attachments = models.FileField(upload_to='medical_records/', blank=True, null=True)

# Inventory Models
class InventoryCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(InventoryCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class InventoryTransaction(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=[('IN', 'IN'), ('OUT', 'OUT')])
    quantity = models.IntegerField()
    transaction_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

# Billing Models
class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])
    issued_date = models.DateField()
    due_date = models.DateField()

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Insurance', 'Insurance')])

# Room Models
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50, choices=[('General', 'General'), ('ICU', 'ICU'), ('Private', 'Private')])
    is_available = models.BooleanField(default=True)

class RoomAllocation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
