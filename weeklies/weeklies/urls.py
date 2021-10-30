from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('contests/', include('contests.urls')),
    path('admin/', admin.site.urls),
]