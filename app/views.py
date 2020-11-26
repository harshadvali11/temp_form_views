from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,FormView,ListView
from django.http import HttpResponse
from app.models import *
#Rendering te Html file with TemplateView class
from app.forms import Student,ProfileForm

class CBV_template(TemplateView):
    template_name='CBV_template.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['data1']='hai this Context data of Template View'
        #context['data2']='THis Django class'
        context['form']=Student()
        return context
    
    def post(self,request):
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))


#get_context_data---->object metod of TemplateView class

#FormView Class
# it better to use FormView class whenever u r dealing with forms
'''
Syntax:

class Class_Name(FormView):
    template_name="name of html file"
    form_class=ClassName_of_form_Class

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))


Note point:
------------
context of form_class will be sent under the name called form 

FormView class is having form_valid object method to validate the Form data
'''

class CBV_FormView(FormView):
    template_name='CBV_formtemplate.html'
    form_class=Student

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))



# Adding data into Models By using Form view class

class CBV_ModelForm(FormView):
    template_name='CBV_modelformtemplate.html'
    form_class=ProfileForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data inserted successfully')




class CBV_ListView(ListView):
    model=Profile
    template_name='CBV_listtemplate.html'
    context_object_name='profileinfo'
    ordering=['name']

































