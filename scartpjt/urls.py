"""
URL configuration for scartpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scartapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar',views.navbar,name='navbar'),
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('account/<int:id>',views.account,name='account'),
    path('addProducts',views.addProducts,name='addProducts'),
    path('search',views.search,name='search'),
     path('viewProducts',views.viewProducts,name='viewProducts'),
    path('viewProdDetail/<int:id>',views.viewProdDetail,name='viewProdDetail'),
    path('addToCart/<int:id>',views.addToCart,name='addToCart'),
    # path('showCart/<int:id>',views.showCart,name='showCart'),
    path('showCart',views.showCart,name='showCart'),
    path('getid',views.getid,name='getid')
]
