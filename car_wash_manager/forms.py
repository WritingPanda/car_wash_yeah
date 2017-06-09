from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer, Service


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "username"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password"
            }
        )
    )


class CustomerForm(forms.Form):
    VEHICLE_TYPE_CHOICES = (
        ("0", "Car"),
        ("1", "Truck"),
        ("2", "Other"),
    )

    attributes = {"class": "form-control"}

    first_name = forms.CharField(
        label="First Name",
        max_length=40,
        min_length=3,
        widget=forms.TextInput(
            attrs=attributes
        )
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=40,
        min_length=2,
        widget=forms.TextInput(
            attrs=attributes
        )
    )
    email_address = forms.EmailField(
        label="Email Address",
        max_length=255,
        min_length=3,
        widget=forms.EmailInput(
            attrs=attributes
        )
    )
    vehicle_type = forms.ChoiceField(
        label="Vehicle Type",
        choices=VEHICLE_TYPE_CHOICES,
        widget=forms.Select(
            attrs=attributes
        )
    )
    license_plate = forms.CharField(
        label="License Plate",
        max_length=10,
        min_length=4,
        widget=forms.TextInput(
            attrs=attributes
        )
    )


class TransactionForm(forms.Form):
    attributes = {"class": "form-control"}

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.Select(
            attrs=attributes
        )
    )
    is_muddy = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    is_bed_let_down = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
