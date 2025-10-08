# import admin
from django.contrib import admin
# import built-in user admin                  
from django.contrib.auth.admin import UserAdmin  
# import our custom model
from .models import CustomUser                      # 

# Register our custom user model so it can be managed via the admin site
admin.site.register(CustomUser, UserAdmin)
