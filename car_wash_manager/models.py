from django.db import models


class BaseModel(models.Model):
    """
    A base model to allow for inheriting created and updated date fields
    """
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Service(BaseModel):
    """
    Describes the type of service and the cost of the service
    """
    car_wash_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=5.00,
        help_text="Price for washing a regular car."
    )
    truck_wash_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=10.00,
        help_text="Price for washing a regular truck."
    )
    additional_charge_cost = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0.00,
        help_text="Additional cost to customer for washing a muddy truck."
    )

    def __str__(self):
        return "Prices"


class Customer(BaseModel):
    """
    Describes the information needed to classify a customer
    """
    VEHICLE_TYPE_CHOICES = (
        ("0", "Car"),
        ("1", "Truck"),
        ("2", "Other"),
    )
    first_name = models.CharField(
        max_length=40,
        help_text="First name of customer."
    )
    last_name = models.CharField(
        max_length=40,
        help_text="Last name of customer."
    )
    email_address = models.EmailField(
        max_length=255,
        help_text="Email address of customer."
    )
    vehicle_type = models.CharField(
        max_length=1,
        choices=VEHICLE_TYPE_CHOICES,
        help_text="The type of vehicle a customer drives."
    )
    license_plate = models.CharField(
        max_length=10,
        help_text="License plate of vehicle."
    )
    times_visited = models.IntegerField(
        help_text="Amount of times customer has been to car wash.",
        default=0
    )
    total_revenue = models.DecimalField(
        help_text="Total amount of money made from customer.",
        default=0,
        decimal_places=2,
        max_digits=5
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Transaction(BaseModel):
    """
    Describes a transaction which is associated with a customer.
    A customer can have multiple transactions.
    """
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="The amount of money paid by the customer."
    )
    additional_charge = models.DecimalField(
        help_text="Additional cost to customer for muddy truck.",
        default=2.00,
        decimal_places=2,
        max_digits=5
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.first_name + " " + str(self.id)

    class Meta:
        ordering = ('-id',)
