# Create your views here.

from django.views.generic import ListView
from django.views.generic import CreateView

from django.core.urlresolvers import reverse

from book.models import Account
from book.models import Verification

class ListAccountView(ListView):
	model = Account

class CreateAccountView(CreateView):
	model = Account

	def get_success_url(self):
		return reverse('accounts-list')

class CreateVerificationView(CreateView):
	model = Verification

	def get_success_url(self):
		return reverse('accounts-list')