from django.contrib import admin

from accounts.models import Profile
# Register your models here.
from .models import *

# accounts
admin.site.register(Profile)
# inventory
admin.site.register(WorkStation)
admin.site.register(State)
admin.site.register(SuppliesType)
admin.site.register(Supply)

