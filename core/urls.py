from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.AccountView.as_view(), name="account"),
    path('expenses/<int:account_id>/', views.Expenses,name="expenses" ),
    path('set_balance', views.CreateBalance.as_view(), name="create_balance"),
    path('', views.CreateOwner.as_view(), name="add_owner"),

]

