"""trustcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app import views
from trustcart import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name="index"),
    path('signup/',TemplateView.as_view(template_name="signup.html"),name="signup"),
    path('login/',TemplateView.as_view(template_name="login.html"),name="login"),
    path('register/',views.register,name="register"),
    path('login_check/',views.logincheck,name="login_check"),
    path('logout/',views.logout,name="logout"),
    path('view_all_mobiles/',views.ViewAllMobiles.as_view(),name="view_all_mobiles"),
    path('view_all_laptops/',views.ViewAllLaptops.as_view(),name="view_all_laptops"),
    path('view_all_Cameras/',views.ViewAllCameras.as_view(),name="view_all_cameras"),
    path('view_all_tvs/',views.ViewAllTvs.as_view(),name="view_all_tvs"),
    path('view_one_mobile/',views.ViewOneMobile.as_view(),name="view_one_mobile"),
    path('view_one_laptop/',views.ViewOneLaptop.as_view(),name="view_one_laptop"),
    path('view_one_camera/',views.ViewOneCamera.as_view(),name="view_one_camera"),
    path('view_one_tv/',views.ViewOneTv.as_view(),name="view_one_tv"),
    path('cart/',views.Cart.as_view(),name="cart"),
    path('remove_cart/',views.RemoveCart.as_view(),name="remove_cart"),
    path('orders/',views.Orders_a.as_view(),name="orders"),
    path('Save/',views.save,name="Save"),
    path('profile/',views.profile,name="profile"),
    path('profile_edit/',views.profile_edit,name="profile_edit"),
    path('update_user/',views.update_user,name="update_user"),
    path('user_delete/',views.user_delete,name="user_delete"),
    path('giftcard/',views.giftcard,name="giftcard"),
    path('giftcard_payment/',views.giftcard_payment,name="giftcard_payment"),
    path('giftcard_save/',views.giftcard_save,name="giftcard_save"),
    path('add_giftcard/',views.add_giftcard,name="add_giftcard"),
    path('add_giftcard_account/',views.add_giftcard_account,name="add_giftcard_account"),
    path('save_address/',views.save_address,name="save_address"),
    path('add_address/',views.add_address,name="add_address"),
    path('update_address/',views.update_address,name="update_address"),
    path('address/',views.address,name="address"),
    path('edit_address/',views.edit_address,name="edit_address"),
    path('buynow_qty/',views.buynow_qty,name="buynow_qty"),
    path('order_summary/',views.order_summary,name="order_summary"),
    path('payments/',views.payments,name="payments"),
    path('delete_address/',views.delete_address,name="delete_address"),
    path('savedcards/',views.savedcards,name="savedcards"),
    path('add_card/',views.add_card,name="add_card"),
    path('card_save/',views.card_save,name="card_save"),
    path('delete_card/',views.delete_card,name="delete_card"),
    path('save_order/',views.save_order,name="save_order"),
    path('invoice/',views.invoice,name="invoice"),
    path('search/',views.Search.as_view(),name="search"),
    path('pin/',views.pin),
    path('about/',views.about,name="about"),
    path('terms_conditions/',TemplateView.as_view(template_name="terms_and_conditions.html"),name="terms_conditions"),
    path('faq/',TemplateView.as_view(template_name="faq.html"),name="faq"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)