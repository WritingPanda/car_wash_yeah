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
    car_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Price for washing a regular car."
    )
    truck_price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text="Price for washing a regular truck."
    )


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
    total_revenue = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="The amount of revenue from a single customer."
    )
    times_visited = models.IntegerField(
        help_text="Amount of times customer has been to car wash."
    )

    def __str__(self):
        return "Name: {first} {last}\nVehicle: {car}\nVisits: {num}\nRevenue: {total}".format(
            first=self.first_name,
            last=self.last_name,
            car=self.vehicle_type,
            num=self.times_visited,
            total=self.total_revenue
        )
