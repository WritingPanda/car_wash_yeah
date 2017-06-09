from django.conf.urls import url
from django.contrib.auth import views

from .forms import LoginForm
from .views import index, dashboard, new_customer, new_transaction


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^login/',
        views.login,
        {
            "template_name": "car_wash_manager/login.html",
            "authentication_form": LoginForm
        },
        name="login"
        ),
    url(r'^logout/', views.logout, {'next_page': '/login'}, name="logout"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^new_customer/$', new_customer, name="new_customer"),
    url(r'^new_transaction/$', new_transaction, name="new_transaction"),
]
