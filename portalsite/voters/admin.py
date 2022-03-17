from django.contrib import admin
from .models import User, Admin, Voter, Precinct
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Voter)
admin.site.register(Precinct)