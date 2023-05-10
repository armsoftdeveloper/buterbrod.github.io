from modeltranslation.translator import register, TranslationOptions
from .models import * 

#--------------------------------------------- All Translation Options ---------------------------------------------#


@register(IndexPageSlider)
class IndexPageSliderTranslationOptions(TranslationOptions):
    fields = ('slider_title',)

@register(IndexPageAssortment)
class IndexPageAssortmentTranslationOptions(TranslationOptions):
    fields = ('assortment_title',)

@register(IndexPageReviews)
class IndexPageReviewsTranslationOptions(TranslationOptions):
    fields = ('review','customer_info')

@register(IndexPageRefreshedMenu)
class IndexPageRefreshedMenuTranslationOptions(TranslationOptions):
    fields = ('refreshed_menu_item_title','refreshed_menu_item_text')

@register(MenuCategories)
class MenuCategoriesTranslationOptions(TranslationOptions):
    fields = ('category',)

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('cat_name','menu_item_name','menu_item_title',)

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('about_us_txt',)
