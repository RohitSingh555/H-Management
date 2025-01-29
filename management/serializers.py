from rest_framework import serializers
from .models import Address, Role, Department, Employee, Patient, Appointment, Prescription, MedicalRecord, InventoryCategory, InventoryItem, InventoryTransaction, Invoice, Payment, Room, RoomAllocation


# Address Serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


# Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


# Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    address = AddressSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        employee = Employee.objects.create(address=address, **validated_data)
        return employee


# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        patient = Patient.objects.create(address=address, **validated_data)
        return patient


# Appointment Serializer
class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = EmployeeSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)
        return appointment


# Prescription Serializer
class PrescriptionSerializer(serializers.ModelSerializer):
    appointment = AppointmentSerializer(read_only=True)

    class Meta:
        model = Prescription
        fields = '__all__'


# MedicalRecord Serializer
class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = '__all__'


# InventoryCategory Serializer
class InventoryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCategory
        fields = '__all__'


# InventoryItem Serializer
class InventoryItemSerializer(serializers.ModelSerializer):
    category = InventoryCategorySerializer(read_only=True)

    class Meta:
        model = InventoryItem
        fields = '__all__'


# InventoryTransaction Serializer
class InventoryTransactionSerializer(serializers.ModelSerializer):
    item = InventoryItemSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = InventoryTransaction
        fields = '__all__'


# Invoice Serializer
class InvoiceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        invoice = Invoice.objects.create(**validated_data)
        return invoice


# Payment Serializer
class PaymentSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


# RoomAllocation Serializer
class RoomAllocationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = RoomAllocation
        fields = '__all__'

    def create(self, validated_data):
        room_allocation = RoomAllocation.objects.create(**validated_data)
        return room_allocation
