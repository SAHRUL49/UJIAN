from django.contrib import admin
from django.urls import path
from kelas.views import kelas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kelas/', kelas),
]
