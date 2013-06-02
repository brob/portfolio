from django.db import models

class Project(models.Model):
	"""(project description)"""
	name = models.CharField(max_length=256)
	slug = models.SlugField(blank=True)
	description = models.TextField(blank=True)
	skill = models.ManyToManyField('Skill', blank=True, null=True)
	
	featured = models.BooleanField(blank=True)

	@models.permalink
	def get_absolute_url(self):
		return ('projects.views.projectDetail', (), {'slug': self.slug,})

	
	class Admin:
		list_display = ('name',)
		search_fields = ('',)


	def __unicode__(self):
		return u'%s' % (self.name)
		
	
class Skill(models.Model):
	"""(project description)"""
	name = models.CharField(max_length=256)
	slug = models.SlugField(blank=True)
	description = models.TextField(blank=True)


	class Admin:
		list_display = ('name',)
		search_fields = ('',)


	def __unicode__(self):
		return u'%s' % (self.name)