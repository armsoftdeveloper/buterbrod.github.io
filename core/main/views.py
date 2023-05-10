# Import Django Shortcuts
from django.shortcuts import render
# Import View
from django.views.generic import ListView
# Import All Models
from .models import * 
# Import All Forms
from .forms import *
# For Contact Form
from django.http import JsonResponse
from django.core import serializers
from django.core.mail import EmailMessage
# Data Mixin
from .utils import *


#--------------------------------------------- All Views ---------------------------------------------#

#Index Page List View Start 

class IndexListView(ListView , DataMixin):
    template_name = 'index.html'

    def get(self , request):
        c_def = self.get_user_context(title = 'Buterbrod')
        indexPageSlider = IndexPageSlider.objects.all()
        about = About.objects.get()
        indexPageAssortment = IndexPageAssortment.objects.all()
        indexPageReviews= IndexPageReviews.objects.all()
        indexPageRefreshedMenu = IndexPageRefreshedMenu.objects.all()

        context = {
            'indexPageSlider':indexPageSlider,
            'about':about,
            'indexPageAssortment':indexPageAssortment,
            'indexPageReviews':indexPageReviews,
            'indexPageRefreshedMenu':indexPageRefreshedMenu,
        }

        context = dict(list(context.items()) + list(c_def.items()))
        return render(request , self.template_name , context)
    
#Index Page List View End 

#---------------------------------------------------------------------------------------------------------

#Menu List View Start 

class MenuListView(ListView , DataMixin):
    template_name = 'menu.html'
    def get(self , request):
        c_def = self.get_user_context(title = 'Buterbrod')
        menu = Menu.objects.all()
        pagePicture = PagePictures.objects.get(id = 1)
        menuCategories = MenuCategories.objects.all()
        
        context = {
            'menu':menu,
            'menuCategories':menuCategories,
            'pagePicture':pagePicture
        }

        context = dict(list(context.items()) + list(c_def.items()))
        return render(request , self.template_name , context)
    
    
#Menu List View End 

#---------------------------------------------------------------------------------------------------------

#About Us List View Start

class AboutUsListView(ListView , DataMixin):
    template_name = 'about.html'
    model = About

    def get(self , request):
        c_def = self.get_user_context(title = 'Buterbrod')
        pagePicture = PagePictures.objects.get(id = 2)
        about = About.objects.get()
        
        context = {
            'about':about,
            'pagePicture':pagePicture
        }

        context = dict(list(context.items()) + list(c_def.items()))
        return render(request , self.template_name , context)
    
#About Us List View End 

#---------------------------------------------------------------------------------------------------------

#Contact List View Start
 
class ContactListView(ListView , DataMixin):
    template_name = 'contact.html'

    def get(self, request):
        c_def = self.get_user_context(title = 'Buterbrod')
        form = Message()
        pagePicture = PagePictures.objects.get(id = 3)

        context = {
            'form':form,
            'pagePicture':pagePicture
        }

        context = dict(list(context.items()) + list(c_def.items()))
        return render(request , self.template_name , context)
    
#Contact List View End

#---------------------------------------------------------------------------------------------------------

# Post Message & Email Handlers Start

def postMessage(request):
    if request and request.method == "POST":
        subject = 'Նոր Նամակ {} - ից'.format(request.POST['name'])
        body = '\nԱնուն Ազգանուն: {}\nԷլ-Փոստ: {}\nՀեռ․Համար: {} \nՆամակ: {}'.format(request.POST['name'], request.POST['email'], request.POST['phone'] , request.POST['txt'])
        try:
            email = EmailMessage(
            subject = subject,
            body = body,
            from_email=request.POST['email'],
            to=["example@gmail.com"],
            )
            email.send()
        except Exception:
            print(Exception)
        form = Message(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": ""}, status=400)


# Post Message & Email Handlers End

#---------------------------------------------------------------------------------------------------------

# Page Not Found Start 

def pageNotFound(request, exception):
    return render(request , '404.html')

# Page Not Found End


    