"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from homework.views import homework, hw_2, show_meetings, show_goals_for_month
from main.views import homepage, test, second

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('test/', test, name='test'),
    path('test2/', second),
    path('homework/', homework, name='homework'),
    path('hw/', hw_2, name='hw'),
    path('meetings/', show_meetings),
    path('mygoals/', show_goals_for_month),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
