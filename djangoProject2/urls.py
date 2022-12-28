"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import APP
from APP import views
from APP.api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', APP.views.home, name="home"),
    path('outbox/', APP.views.outbox, name="outbox"),
    path('massages/', APP.views.massage, name="massages"),#inbox
    path('unread/', APP.views.unread, name="unread"),



    path('read_massage/<str:pk>/', APP.views.readmassage_inbox, name="read_massage_inbox"),
    path('read_outbox/<str:pk>/', APP.views.readmassage_outbox, name="read_massage_outbox"),
    path('read_unraed/<str:pk>/', APP.views.readmassage_unread, name="read_massage_unread"),

    path('massages/<str:pk>/', APP.views.deleteMassage_inbox, name="delete_massage_inbox"),
    path('outbox/<str:pk>/', APP.views.deleteMassage_inbox, name="delete_massage_outbox"),
    path('unread/<str:pk>/', APP.views.deleteMassage_unread, name="delete_massage_unread"),

    path('login/', APP.views.loginPage, name="login"),
	path('logout/', APP.views.logoutUser, name="logout"),

    # api view
    path('api_massage/', APP.api.views.MassageCreatAPIView.as_view(), name="create_massage"),


]
