from django.contrib import admin
from .models import *
from .adminUtils import *

#--------------------------------------------- Registering ---------------------------------------------#

admin.site.register(BasicModel , BasicModel_Display)
admin.site.register(PagePictures , PagePictures_Display)
admin.site.register(IndexPageSlider , IndexPageSlider_Display)
admin.site.register(IndexPageAssortment , IndexPageAssortment_Display)
admin.site.register(IndexPageRefreshedMenu , RefreshedMenu_Display)
admin.site.register(IndexPageReviews , Reviews_Display)
admin.site.register(MenuCategories , MenuCategories_Display)
admin.site.register(Menu , Menu_Display)
admin.site.register(About , About_Display)
admin.site.register(TermsAndConditions , Terms_Admin)
admin.site.register(Get_message , Get_message_Display)


