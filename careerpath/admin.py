from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Field, Subfield, Skill, JobExample, LearningResource, RealWorldProject

# Register your models here.
admin.site.register(Field)
admin.site.register(Subfield)
admin.site.register(Skill)
admin.site.register(JobExample)
admin.site.register(LearningResource)
admin.site.register(RealWorldProject)