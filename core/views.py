from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from django.views.generic import FormView
#from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Create your views here.
class AccountView(ListView):
    model = models.Account
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        owner_account = models.Owner.objects.filter(user_name_id= self.request.owner.id)
        context = super(AccountView, self).get_context_data(*args, **kwargs)
        context["owner_account"] = owner_account
        return context 


def Expenses(request, account_id):
    balance = models.Account.objects.get(id=account_id)
    savings = 0.25 * balance.balance
    house = 0.25 * balance.balance
    jaiye = 0.05 *  balance.balance
    grocery = 0.20 * balance.balance
    wardrobe = 0.10 * balance.balance
    unforseen = 0.15 * balance.balance

    context = {'house':house, 'balance': balance, 'jaiye': jaiye, 'unforseen':unforseen, 'closet':wardrobe, 'savings': savings, 'grocery':grocery}

    return render(request, 'core/account.html', context)

class CreateBalance(CreateView):
    model = models.Account
    template_name = 'core/create_account.html'
    form_class = forms.AccoutnForm
    success_url = '/'

class CreateOwner(CreateView):
    model = models.Owner
    template_name = 'core/create_owner.html '
    form_class = forms.OwnerForm
    success_url = '/'