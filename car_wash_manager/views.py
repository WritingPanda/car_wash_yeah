from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomerForm, TransactionForm
from .models import Customer, Transaction, Service


MESSAGE_TAGS = {
    messages.SUCCESS: 'success',
    messages.ERROR: 'danger'
}


def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, template_name="car_wash_manager/index.html")


@login_required(login_url="login/")
def dashboard(request):
    customer_list = Customer.objects.all()
    transaction_list = Transaction.objects.all()

    total_revenue = Transaction.objects.aggregate(Sum('amount'))

    context = {
        "customer_list": customer_list,
        "transaction_list": transaction_list,
        "total_revenue": total_revenue['amount__sum']
    }
    return render(request, template_name="car_wash_manager/dashboard.html", context=context)


@login_required(login_url="login/")
def new_customer(request):
    form = CustomerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            vehicle_type = form.cleaned_data['vehicle_type']
            license_plate = form.cleaned_data['license_plate']
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email_address=email_address,
                vehicle_type=vehicle_type,
                license_plate=license_plate
            )
            customer.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Customer has been saved as {} {}".format(first_name, last_name)
            )
            return redirect('dashboard')
    else:
        context = {
            "form": form
        }
        return render(request, template_name="car_wash_manager/new_customer.html", context=context)


@login_required(login_url="login/")
def new_transaction(request):
    form = TransactionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # Get prices
            prices = Service.objects.get(pk=1)
            car_price = prices.car_wash_price
            truck_price = prices.truck_wash_price

            # Clean form data
            customer = form.cleaned_data['customer']
            is_muddy = form.cleaned_data['is_muddy']
            is_bed_let_down = form.cleaned_data['is_bed_let_down']

            # Get current customer
            customer_instance = get_object_or_404(Customer, pk=customer.id)

            # Check if the car is stolen
            if customer_instance.license_plate == "1111111":
                messages.error(request, "This vehicle has been stolen. Do not serve the customer.")
                return redirect('dashboard')

            # Determine charge based on vehicle
            if customer_instance.vehicle_type == "2":
                messages.error(request, "We do not service this type of vehicle, only cars and trucks.")
                return redirect('dashboard')
            elif customer_instance.vehicle_type == "0":
                amount = car_price
            elif customer_instance.vehicle_type == "1":
                amount = truck_price
            else:
                messages.error(request, "Invalid vehicle.")
                return redirect('dashboard')

            if is_bed_let_down:
                messages.error(request, "The truck's bed is let down. We cannot wash it.")
                return redirect('dashboard')

            customer_instance.times_visited += 1

            # Will discount the base price of the car wash
            # If truck is muddy, we will add the two dollars after the discount
            if customer_instance.times_visited == 2:
                amount = amount / 2

            # We do not care if the customer has a car that is muddy. However, if the truck bed is muddy,
            # we will increase the price by two dollars. Otherwise, we move along.
            if is_muddy and customer_instance.vehicle_type == "1":
                # Get the price for the extra charge
                extra_charge = prices.additional_charge_cost
                amount = amount + extra_charge
            else:
                # If there is no need for an extra charge on the vehicle, set it to 0.00
                extra_charge = 0.00

            customer_instance.total_revenue = customer_instance.total_revenue + amount

            # Get the model ready for saving
            transaction_instance = Transaction(amount=amount, customer=customer, additional_charge=extra_charge)

            transaction_instance.save()
            customer_instance.save()

            messages.success(request, "Transaction saved successfully.")
            return redirect('dashboard')
    else:
        context = {
            "form": form
        }
        return render(request, template_name="car_wash_manager/new_transaction.html", context=context)
