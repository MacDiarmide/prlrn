"""
URL configuration for my_first_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import hello_world, hello_world_2, render_page, render_page_2
from crm import views  # Python подсвечивает этот код как неправильный, но он все равно работает
from .settings import DEBUG  # это нужно для dev-версии

urlpatterns = [
    path('admin/', admin.site.urls),  # первый аргумент - это путь в адресной строке, а второй - функция из views
    path('hello_world/', hello_world),
    path('hello_world_2/', hello_world_2),
    path('render_page/', render_page),
    path('render_page_2/', render_page_2),
    path('query_set/', views.query_set),  # странный способ ссылки на функцию
    path('thanks_page/', views.thanks_page, name='thanks_page'),  # третий аргумент нужен для правильной ссылки из формы на другой странице
    path('inheritance_page/', views.inheritance_page),
    path('thanks_2/', views.thanks_2, name='thanks_2'),  # три дня я не мог понять, в чем дело, а дело было в третьем аргументе здесь!!!
    path('', views.site_view),  # пустой путь означает, что данная функция отображается после имени домена
]

# все, что далее, нужно для dev-версии
if DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
