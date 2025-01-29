from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Initialize the router
router = DefaultRouter()

# Register the viewsets with the router
router.register(r'addresses', views.AddressViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'prescriptions', views.PrescriptionViewSet)
router.register(r'medical-records', views.MedicalRecordViewSet)
router.register(r'inventory-categories', views.InventoryCategoryViewSet)
router.register(r'inventory-items', views.InventoryItemViewSet)
router.register(r'inventory-transactions', views.InventoryTransactionViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'room-allocations', views.RoomAllocationViewSet)

# Define the URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # API Routes for all models
]
