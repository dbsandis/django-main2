from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'User/Profile Administration'  # Customize the admin site header
    site_title = 'Electronic Recovery Home Tracker'  # Customize the title shown on the browser tab
    index_title = 'Welcome to ERHT Administration'  # Customize the index page title

# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name='customadmin')

