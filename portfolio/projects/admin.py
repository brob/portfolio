from django.contrib import admin
from projects.models import *


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prepopulated_fields = {"slug": ("name",)}

class SkillAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prepopulated_fields = {"slug": ("name",)}

				
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
