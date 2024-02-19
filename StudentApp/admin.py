from django.contrib import admin

from StudentApp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.CollegeAdmin)
admin.site.register(models.Marks)