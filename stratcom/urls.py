from django.urls import path
from . import views

urlpatterns = [
    path('',views.index5, name = "index"),
    path('signup1/',views.signup1, name ="signup"),
    path('signup2/',views.signup2, name ="signup"),
    path('signup3/',views.signup3, name ="signup"),
    path('signup4/',views.signup4, name ="signup"),
    path('index1/',views.index1, name ="signup"),
    path('index2/',views.index2, name ="signup"),
    path('index3/',views.index3, name ="signup"),
    path('index4/',views.index4, name ="signup"),
    path('index5/',views.index1, name ="signup"),
    path('gallery1/',views.gallery1, name ="signup"),
    path('gallery2/',views.gallery2, name ="signup"),
    path('gallery3/',views.gallery3, name ="signup"),
    path('gallery4/',views.gallery4, name ="signup"),
    path('about/',views.aboutus, name ="about"),
    path('homepage/',views.homepage, name ="homepage"),
]