from django.urls import path,include
from . import views
from unicodedata import name 

urlpatterns = [
    path('',views.home,name='home'),
    
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('crud',views.crud,name='crud'),
    path('add_details',views.add_details,name='add_details'),
    path('show_products',views.show_products,name='show_products'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_Product_Details/<int:pk>',views.edit_Product_Details,name='edit_Product_Details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
   
    
    
]
    