
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', include('dashboard.urls')),
    path('', include('LearTrack_app.urls'))
]
