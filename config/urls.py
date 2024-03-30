"""
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
