from django.db import models

#--------------------------------------------- All Models ---------------------------------------------#

# Basic Model Start 

class BasicModel(models.Model):
    page_logo = models.ImageField(("Ներբեռնել Նկար"), upload_to="media/%Y/%md/%d")
    food_zone_address = models.CharField(("Հասցե"), max_length=70)
    food_zone_phone = models.CharField(("Հեռ․համար"), max_length=50)
    food_zone_email = models.EmailField(("Էլ-հասցե"), max_length=254)
    food_zone_work_hours_start = models.CharField(("Աշխ․սկիզբ"), max_length = 70 , null = True)
    food_zone_work_hours_end = models.CharField(("Աշխ․ավարտ"), max_length = 70 , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)

    def __str__(self):
        return "Ղեկավարման Կետ"
    
    class Meta:
        verbose_name = "Ղեկավարման Կետ"
        verbose_name_plural = "Ղեկավարման Կետ"

# Basic Model End 

# Page Pictures Start

class PagePictures(models.Model):
    picture = models.ImageField(("Ներբեռնել Նկար"), upload_to="media/%Y/%md/%d")
    decription = models.CharField(("Էջի Անուն"), max_length=50 , null = True)

    def __str__(self):
        return "Էջերի Պատկերներ"
    
    class Meta:
        ordering = ['id']
        verbose_name = "Էջերի Պատկերներ"
        verbose_name_plural = "Էջերի Պատկերներ"


# Page Pictures End

# Index Page Models Start 

class IndexPageSlider(models.Model):
    slider_img = models.ImageField(("Նկար"), upload_to="media/%Y/%m/%d")
    slider_title = models.CharField(("Վերնագիր"), max_length=50)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)
    is_published = models.BooleanField(("Տեղադրված է ՞ ") , default=True , null=True)

    def __str__(self):
        return self.slider_title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Գլխավոր Սլայդեր"
        verbose_name_plural = "Գլխավոր Սլայդեր"

class IndexPageAssortment(models.Model):
    assortment_img = models.ImageField(("Նկար"), upload_to="media/%Y/%m/%d" , null = True)
    assortment_title = models.CharField(("Տեսականու Վերնագիր"), max_length=50 , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)
    is_published = models.BooleanField(("Տեղադրված է ՞ ") , default=True , null=True)

    def __str__(self):
        return "Տեսականի"
    
    class Meta:
        ordering = ['id']
        verbose_name = "Տեսականի"
        verbose_name_plural = "Տեսականի"

class IndexPageRefreshedMenu(models.Model):
    refreshed_menu_item_image = models.ImageField(("Նկար"), upload_to="media/%Y/%m/%d")
    refreshed_menu_item_title = models.CharField(("Վերնագիր"), max_length=50)
    refreshed_menu_item_text = models.CharField(("Տեքստ"), max_length=50)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)
    is_published = models.BooleanField(("Տեղադրված է ՞ ") , default=True , null=True)

    def __str__(self):
        return self.refreshed_menu_item_title
    
    class Meta:
        ordering = ['id']
        verbose_name = "Թարմացված Մենյու"
        verbose_name_plural = "Թարմացված Մենյու"
    
class IndexPageReviews(models.Model):
    review = models.TextField(("Մեկնաբանություն"))
    customer_info = models.CharField(("Անուն Ազգանուն"), max_length=50)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)
    is_published = models.BooleanField(("Տեղադրված է ՞ ") , default=True , null=True)
    
    def __str__(self):
        return self.customer_info
    
    class Meta:
        ordering = ['id']
        verbose_name = "Կարծիքների Սլայդեր"
        verbose_name_plural = "Կարծիքների Սլայդեր"

# Index Page Models End 

# Menu Page Model Start

class MenuCategories(models.Model):
    category = models.CharField(("Կատեգորիայի Անուն"), max_length=50)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['id']
        verbose_name = "Մենյու Կատեգորիաներ"
        verbose_name_plural = "Մենյու Կատեգորիաներ"

class Menu(models.Model):
    cat_name = models.ForeignKey(MenuCategories, related_name="cat", on_delete=models.CASCADE)
    menu_img = models.ImageField(("Նկար"), upload_to="media/%Y/%m/%d")
    menu_item_name = models.CharField(("Վերնագիր"), max_length=50)
    menu_item_title = models.CharField(("Տեքստ"), max_length=50)
    menu_item_price = models.IntegerField(("Գին") , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)
    is_published = models.BooleanField(("Տեղադրված է ՞") , default = True , null = True)

    def __str__(self):
        return self.menu_item_name
    
    class Meta:
        ordering = ['id']
        verbose_name = "Մենյու"
        verbose_name_plural = "Մենյու"

# Menu Page Model End

# About Page Model Start

class About(models.Model):
    about_us_img = models.ImageField(("Նկար"), upload_to="media/%Y/%m/%d")
    about_us_title = models.CharField(("Վերնագիր"), max_length=50)
    about_us_txt = models.TextField(("Մեր Մասին Տեքստ"))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)
    is_published = models.BooleanField(("Տեղադրված է ՞") , default = True , null = True)

    def __str__(self):
        return "Մեր Մասին"
    
    class Meta:
        verbose_name = "Մեր Մասին"
        verbose_name_plural = "Մեր Մասին"

# About Page Model End

# Terms & Conditions Start 

class TermsAndConditions(models.Model):
    terms_title = models.CharField(("Վերնագիր"), max_length=50)
    description = models.TextField(("Տեքստ") , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծման Ամսաթիվ" , null = True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Փոփոխման Ամսաթիվ" , null = True)

    def __str__(self):
        return "Կայքի Մասին"
    
    class Meta:
        verbose_name = "Կայքի Մասին"
        verbose_name_plural = "Կայքի Մասին"

# Terms & Conditions End 

# Forms Models Start 

class Get_message(models.Model):
    name = models.CharField(("Անուն"), max_length=50)
    email = models.EmailField(("Էլ-Փոստ"), max_length=254)
    phone = models.CharField(("Հեռ․ Համար"), max_length=50)
    txt = models.TextField(("Հաղորդագրություն") , null = True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Ստեղծվելու Ամսաթիվ")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        verbose_name = "Նամակներ"
        verbose_name_plural="Նամակներ"

# Forms Models End 
