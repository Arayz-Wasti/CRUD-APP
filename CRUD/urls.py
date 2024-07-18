from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.CreateView,name='create'),
    path('readview/',views.ReadView,name='readview'),
    path('UpdateView/<int:id>/',views.UpdateView,name='UpdateData'),
    path('delete/<int:id>/',views.DeleteView,name='delete')
]
