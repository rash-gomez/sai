from multiprocessing.reduction import register

from django.contrib import admin

from apply import models

# Register your models here.


admin.site.register(models.Student)
admin.site.register(models.Session)
admin.site.register(models.Field)
admin.site.register(models.Speciality)
admin.site.register(models.Document)
