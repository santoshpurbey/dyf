from django.contrib import admin

# Register your models here.
from .models import Banner, Logo, Footer
admin.site.register(Logo)
admin.site.register(Banner)
admin.site.register(Footer)


