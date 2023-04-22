from django.urls import path
from .views import *



urlpatterns = [
    path('test/', test, name="test"),

    path('test-1/', TestViewClass_1.as_view(), name="TestViewClass_1"),

    path('test-2/', TestViewClass_2.as_view(), name="TestViewClass_2"),

    path('test-3/', TestViewClass_3.as_view(subject="Chemistry"), name="TestViewClass_3"),

    path('sub-t-2/', SubClass.as_view(), name="SubClass"),

    path('test-4/', TestViewClass_4.as_view(), name="TestViewClass_4"),

    path('test-5/', TestViewClass_5.as_view(), name="TestViewClass_5"),

    path('test-6/', TestViewClass_6.as_view(), name="TestViewClass_6"),

    path('test-7/', TestViewClass_7.as_view(), name="TestViewClass_7"),

#----------------------------------------------------Template View--------------------------------------------------------

    path('tv-1/', templateview_1.as_view( template_name="test/TemplateView_1.html" ,extra_context ={'course': 'Django'}), name="templateview_1"), 

    #path('tv-1/<int:id>/', templateview_1.as_view( template_name="test/TemplateView_1.html" ,extra_context ={'course': 'Django'}), name="templateview_1"),

#----------------------------------------------------Redirect View--------------------------------------------------------

    #path('rv-1/', RedirectView_1.as_view(url="http://studentportal.diu.edu.bd/#/dashboard1"), name="RedirectView_1"),
    #path('rv-1/', RedirectView_1.as_view(url="http://127.0.0.1:8000/test/test-6/"), name="RedirectView_1"),
    #path('rv-1/<slug:frute>/', RedirectView_1.as_view(), name="RedirectView_1"),
    #path('rv-1/<int:id>/', RedirectView_1.as_view(), name="RedirectView_1"),
    path('rv-1/', RedirectView_1.as_view(), name="RedirectView_1"),
    #path('rv-1/', RedirectView_1.as_view(pattern_name ="TestViewClass_1"), name="RedirectView_1"),

    # path('<slug:frute>/', templateview_1.as_view( template_name="test/TemplateView_1.html" ,extra_context ={'course': 'Django'}), name="templateview_rv"),
    #path('rv-result/<int:id>/', R_V.as_view(extra_context ={'address': 'Saver'}), name="R_V"),
    path('rv-result/', R_V.as_view(extra_context ={'address': 'Saver'}), name="R_V"),

]