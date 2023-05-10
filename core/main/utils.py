from .models import * 

page_static = [
    {'title':'Գլխավոր','url_name':'home'},
    {'title':'Մենյու','url_name':'menu'},
    {'title':'Մեր Մասին','url_name':'about'},
    {'title':'Կապ Մեզ Հետ','url_name':'contact'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        terms = TermsAndConditions.objects.get()
        basicModel = BasicModel.objects.get()
        context = kwargs
        context['terms'] = terms
        context['basicModel'] = basicModel
        context['page_static'] = page_static
        return context
