from django.contrib import admin
from api.models import *


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(AssignmentUser)
class AssignmentUserAdmin(admin.ModelAdmin):
    pass



