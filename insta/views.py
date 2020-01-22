from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Account
from .main import InstaBot
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager



class HomePageView(CreateView):
	model = Account
	template_name = 'home.html'
	fields = {'user_name', 'password'}
	def submit(request):
		if request.method == 'POST':
			name=request.POST['user_name']
			pasw=request.POST['password']
			driver = webdriver.Chrome(ChromeDriverManager().install())
			global names
			names = InstaBot(str(name),str(pasw)).get_unfollowers()
	def index(request):

		context={nam:names}
		return render(request, 'names.html', context)


class Names(TemplateView):
	template='names.html'

