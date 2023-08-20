from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicleNumber', 'vehicleModel','engineModel', 'engineNumber', 'transmissionModel', 'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber', 'deliveryContract_N_data', 'deliveryDate', 'consignee', 'deliveryAdress', 'completeSet', 'client', 'serviceCompany']
        # fields = [field.name for field in Vehicle._meta.get_fields()]