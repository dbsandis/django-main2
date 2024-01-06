from django.urls import path
from .views import home_view
# import custom_admin_site.urls
from .admin import custom_admin_site
urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', custom_admin_site.urls), 
    
]