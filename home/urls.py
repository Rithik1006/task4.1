from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="CLICKARC"
admin.site.site_title="photography dashboard"
admin.site.index_title="Welcome To This Site"


urlpatterns = [
    path('', views.home,name='home'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('contact/',views.contact,name='contact'),
]