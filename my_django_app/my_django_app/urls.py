from django.contrib import admin
from django.urls import path
from htop_app.views import htop_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop_view),
]
