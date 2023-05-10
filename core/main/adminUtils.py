from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django import forms

#--------------------------------------------- Translation Classes ---------------------------------------------#

class Index_Page_Slider_Admin(TranslationAdmin):
    list_display = ('id', 'slider_img' , 'slider_title' ,'time_create' , 'time_update' , 'is_published')
    list_display_links = ('id', 'slider_title')
    
class Index_Page_Assortment_Admin(TranslationAdmin):
    list_display = ('id', 'assortment_img' , 'assortment_title' , 'time_create' , 'time_update' , 'is_published')
    list_display_links = ('id', 'assortment_title')

class Index_Page_Refreshed_Menu_Admin(TranslationAdmin):
    list_display = ('id', 'refreshed_menu_item_image' , 'refreshed_menu_item_title' , 'refreshed_menu_item_text' , 'time_create' , 'time_update' , 'is_published')
    list_display_links = ('id', 'refreshed_menu_item_title')

class Menu_Admin(TranslationAdmin):
    list_display = ('id', 'cat_name' , 'menu_item_name' , 'menu_item_title' , 'menu_item_price', 'time_create' , 'time_update' ,  'is_published')
    list_display_links = ('id', 'menu_item_name' , 'menu_item_title' , 'time_update' , 'is_published')

class About_Us_Admin(TranslationAdmin):
    list_display = ('id', 'about_us_title' , 'about_us_txt')
    list_display_links = ('id', 'about_us_title' , 'about_us_txt')

#--------------------------------------------- CKEDITOR ---------------------------------------------#

class TermsEditorForm(forms.ModelForm):
    description = forms.CharField(label = "Opisanie" , widget = CKEditorUploadingWidget())

    class Meta:
        model = TermsAndConditions
        fields = '__all__'

class Terms_Admin(admin.ModelAdmin):
    list_display = ('id', 'terms_title' , 'description')
    list_display_links = ('id', 'terms_title' , 'description')
    form = TermsEditorForm


#--------------------------------------------- List Display ---------------------------------------------#

class BasicModel_Display(admin.ModelAdmin):
    list_display = ('id', 'page_logo' , 'food_zone_address' , 'food_zone_phone' , 'food_zone_email' , 'time_create', 'time_update',)
    list_display_links = ('id', 'page_logo' , 'food_zone_address' , 'food_zone_phone' , 'food_zone_email' , 'time_create', 'time_update',)

class PagePictures_Display(admin.ModelAdmin):
    list_display = ('id', 'decription' , 'picture')
    list_display_links = ('id', 'decription' , 'picture')

class IndexPageSlider_Display(admin.ModelAdmin):
    list_display = ('id', 'slider_title' , 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create' , 'time_update')
    list_display_links = ('id', 'slider_title' , 'time_create', 'time_update',)

class IndexPageAssortment_Display(admin.ModelAdmin):
    list_display = ('id', 'assortment_title' , 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create' , 'time_update')
    list_display_links = ('id', 'assortment_title' , 'time_create', 'time_update',)

class RefreshedMenu_Display(admin.ModelAdmin):
    list_display = ('id', 'refreshed_menu_item_title' , 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create' , 'time_update')
    list_display_links = ('id', 'refreshed_menu_item_title' , 'time_create', 'time_update',)

class Reviews_Display(admin.ModelAdmin):
    list_display = ('id', 'customer_info' ,'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create' , 'time_update')
    list_display_links = ('id', 'customer_info' ,'time_create', 'time_update',)

class MenuCategories_Display(admin.ModelAdmin):
    list_display = ('id', 'category' , 'time_create', 'time_update')
    list_filter = ('time_create' , 'time_update')
    list_display_links = ('id', 'category' , 'time_create', 'time_update')

class Menu_Display(admin.ModelAdmin):
    list_display = ('id', 'menu_item_name' , 'menu_item_title' , 'menu_item_price' , 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create' , 'time_update')
    list_display_links = ('id', 'menu_item_name' , 'menu_item_title' , 'menu_item_price' , 'time_create', 'time_update')

class About_Display(admin.ModelAdmin):
    list_display = ('id', 'about_us_title' , 'about_us_txt' , 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create' , 'time_update')
    list_display_links = ('id', 'about_us_title' , 'about_us_txt' , 'time_create' , 'time_update')

class Get_message_Display(admin.ModelAdmin):
    list_display = ('id', 'name' , 'email', 'phone' , 'txt' , 'time_create',)
    list_filter = ('time_create' ,)
    list_display_links = ('id', 'name' , 'email', 'phone' , 'txt' , 'time_create',)