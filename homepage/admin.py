from django.contrib import admin

# Register your models here.
from .models import (
                    Banner, 
                    Logo, 
                    Footer, 
                    WorkingArea,
                    SocialMediaIcon,)
admin.site.register(Logo)
admin.site.register(Banner)
admin.site.register(Footer)
admin.site.register(WorkingArea)
admin.site.register(SocialMediaIcon)

