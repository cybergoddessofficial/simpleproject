from django.urls import path

from myapp import views

urlpatterns = [
   path('',views.homepage,name="homepage"),
   path('index',views.index,name="index"),
   path('sample',views.sample,name="sample"),
   path('samplepage',views.samplepage,name="samplepage"),
   path('reg', views.reg, name="reg"),
   path('student', views.student, name="student"),
   path('savedata',views.savedata,name="savedata"),
   path('register',views.register,name="register"),
   path('registersave',views.registersave,name="registersave"),
   path('imagesave',views.imagesave,name="imagesave"),

]