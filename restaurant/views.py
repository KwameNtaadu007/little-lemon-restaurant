#from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
from restaurant.forms import BookingForm
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

#Create your views here.


def index(request): 
    #welcome = "Welcome to Little Lemon"
    return render(request, 'index.html',{}) 

def login(request): 
    return render(request, '/admin/',{})  

# Create your views here for menu.
def about(request):
    return render(request, "about.html", {})

def menu(request):
    menu_items = Menu.objects.all()
    menu_dict = {'menu':menu_items}
    return render(request, "menu.html", menu_dict)

def display_menu_item(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    return render(request,'menu_item.html',{"menu_item":menu_item})


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/success/')
    context = {"form": form}
    return render(request, "book.html", context)


class SuccessView(TemplateView):
    template_name = "success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["booking"] = self.request.user.booking
        return context

