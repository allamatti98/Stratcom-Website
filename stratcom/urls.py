from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('home/',views.index, name = "index"),
    path('login/',views.login, name = "login"),
    path('signup/',views.signup, name = "signup"),
    path('aboutus/',views.aboutus, name = "aboutus"),
    path('ourteam/',views.ourteam, name = 'ourteam'),
    path('upcomingevents/',views.upcomingevents, name = "upcomingevents"),
    path('pastevents/',views.pastevents, name = "pastevents"),
    path('galleryfullwidth/',views.galleryfullwidth, name = "galleryfullwidth"),
    path('gallerygrid/',views.gallerygrid, name = "gallerygrid"),
    path('ourcourses/',views.ourcourses, name = "ourcourses"),
    path('directcall/',views.directcall, name = "directcall"),
    path('sendemail/',views.sendemail, name = "sendemail"),
    path('suggestionsbox/',views.suggestionsbox, name = "suggestionsbox"),
    path('applyforinternship/',views.applyforinternship,name = "applyforinternship"),
    path('userprofile/',views.userprofile, name = "userprofile"),
    path('logout/',views.logout, name = "logout")

    # path('useraccounts/'views.useraccount, name = "accountpage")
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)