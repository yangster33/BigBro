"""BigBro URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.decorators import login_required


from user.views import MyLogin, MyLogout, TestView, MyPasswordChangeView
from .settings import MEDIA_ROOT
from costs.views import IndexView, FlowsView, ChartsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyLogin.as_view(), name='login'),
    path('logout/', MyLogout.as_view(), name='logout'),
    path('changepassword/', login_required(MyPasswordChangeView.as_view()), name='changepassword'),
    path('test/', TestView.as_view(), name='test'),
    path('index/', login_required(IndexView.as_view()), name='index'),
    path('charts/', login_required(ChartsView.as_view()), name='charts'),
    path('flows/', login_required(FlowsView.as_view()), name='flows'),
    # path('media/<str:path>/', serve, {"document_root":MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] 


# print(settings.MEDIA_URL, settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  


