from django import forms
from .models import Target

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'latitude', 'longitude', 'date_expiry']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nome'
    )
    latitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Latitude',
        min_value=-90,
        max_value=90,
        decimal_places=6
    )
    longitude = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Longitude',
        min_value=-180,
        max_value=180,
        decimal_places=6
    )
    date_expiry = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        label='Data de expiração'
    )