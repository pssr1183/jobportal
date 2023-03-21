from django.urls import path
from . import views
urlpatterns = [
    path('',views.show,name="main"),
    # path('display',views.display,name='display')
    path('view',views.disView.as_view(),name='show'),
    path('view',views.TempList.as_view(),name='show'),
    path('register',views.register,name='register'),
    
    
]