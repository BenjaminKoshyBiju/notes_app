from .import views
from django.urls import path
urlpatterns = [
     path('',views.index.as_view(),name='notes'),
     path('modify/<str:note_id>/',views.modify.as_view(),name='mod'),
    
]
