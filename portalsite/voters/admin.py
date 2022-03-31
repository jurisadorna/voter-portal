from django.contrib import admin
from .models import User, Admin, Voter, Precinct, Rep, Faci
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Voter)
admin.site.register(Precinct)
admin.site.register(Rep)
admin.site.register(Faci)