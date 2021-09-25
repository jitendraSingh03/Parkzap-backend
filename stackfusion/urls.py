from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-view/',views.contactList.as_view()),
    path("",views.contactCreate.as_view(),name='home')
]