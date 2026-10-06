from django.shortcuts import render
from .product_data import side_bar_data , footer_data
def home(request):
    return render(request, 'home.html' , {"data": side_bar_data.menu_data , "data": footer_data.data} )