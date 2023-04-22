from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from .models import *

from django.views.generic.base import TemplateView, RedirectView
from django.views import View

from django.db.models import Q


# Create your views here.

def test(request):
    return render(request, "test.html")
#------------------------------------------------- View -----------------------------------------------------
class TestViewClass_1(View):
    def get(self, request):
        return HttpResponse('<h1>Rakib<h1>')
    
class TestViewClass_2(View):
    subject="Physics"
    def get(self, request):
        return HttpResponse(self.subject)
    
class TestViewClass_3(View):
    #subject="Physics"
    subject=""
    def get(self, request):
        return HttpResponse(self.subject)
    

class SubClass(TestViewClass_2):
    def get(self, request):
        return HttpResponse(self.subject)
    

class TestViewClass_4(View):
    # student_list={
    #     "name": "",
    #     "age": "",
    #     "study": "",
    # }
    def get(self, request):
        return render(request, "test/test_1.html")
    
    def post(self, request):
        n=request.POST.get("name")
        a=request.POST.get("age")
        s=request.POST.get("study")
        # print("---------------------------------------")
        # print(f"Name: {n}, Age: {a}, Study: {s}")
        # print("---------------------------------------")

        student_list={
            "name": n,
            "age": a,
            "study": s,
        }

        return render(request, "test/test_1.html", student_list)
    

class TestViewClass_5(View):
    student_name = []
    def get(self, request):
        data = {"std": self.student_name}
        return render(request, "test/test_2.html", data)
    
    def post(self, request):
        n=request.POST.get("name")
        self.student_name.append(n)
        data = {"std": self.student_name}
        return render(request, "test/test_2.html",data)
    

class TestViewClass_6(View):
    student_list={
        "name": "",
        "age": "",
    }
    def get(self, request):
        data = {"std": self.student_list}
        return render(request, "test/test_3.html", data)
    
    def post(self, request):
        n=request.POST.get("name")
        a=request.POST.get("age")

        self.student_list["name"]=n
        self.student_list["age"]=a

        data = {"std": self.student_list}        

        return render(request, "test/test_3.html",data)
        

class TestViewClass_7(View):
    student_list = {}
    def get(self, request):
        data = {"std": self.student_list}
        return render(request, "test/test_4.html", data)
    
    def post(self, request):
        for i in range(3):
            key=request.POST.get("key")
            value=request.POST.get("value")
            self.student_list.update({key : value})

        data = {"std": self.student_list}        

        return render(request, "test/test_4.html",data)
    
#---------------------------------------------------Template View----------------------------------------------------

# TemplateResponseMixin, ContextMixin, View
class templateview_1(TemplateView): 
    #template_name = "test/TemplateView_1.html"
    template_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Rakib'
        context['roll'] = 1515
        # print("---------------------------")
        # print(kwargs)
        # print("---------------------------")

        # context = {
        #     'name': "Rakib",
        #     'roll': 1515,
        # }
        return context
    
#---------------------------------------------------Redirect View----------------------------------------------------
class RedirectView_1(RedirectView): 
    #url="http://127.0.0.1:8000/test/test-6/"
    #url="/test/test-6/"
    pattern_name ="R_V"
    #pattern_name = ""
    permanent = True #By Deffault it's False
    query_string =True #By Deffault it's False

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
    
class R_V(TemplateView):
    template_name = "test/RedirectView_1.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["name"] = "Md Rasel"
        data["Profesion"] = "Django Developer"

        # data = {
        #     "name": "Md Rasel",
        #     "Profesion": "Django Developer",
        # }

        return data
