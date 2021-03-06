from django.contrib import admin
from .models import *
from easy_select2 import select2_modelform

class ProjectLinkInline(admin.TabularInline):
    model = ProjectLink
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fields = (('name','members'),('tagline','topics'),('published','cover'),'detail')
    inlines = (ProjectLinkInline,)
    select2 = select2_modelform(Project, attrs={'width': '250px'})
    form = select2

class CertificateAdmin(admin.ModelAdmin):
    fields = ('title',('member','issuer'),('date','attachment'),'topics')
    select2 = select2_modelform(Certificate, attrs={'width': '250px'})
    form = select2

class CourseAdmin(admin.ModelAdmin):
    fields = (('name','issuer'),('member','certificate'),('topics','url'))
    select2 = select2_modelform(Course, attrs={'width': '250px'})
    form = select2

class HonourAdmin(admin.ModelAdmin):
    fields = (('title','issuer'),('member','date'),('project','certificate'),('topics','url'))
    select2 = select2_modelform(Honour, attrs={'width': '250px'})
    form = select2

class PublicationAdmin(admin.ModelAdmin):
    fields = (('title','publisher'),('members','date'),('project','url'),'topics')
    select2 = select2_modelform(Publication, attrs={'width': '250px'})
    form = select2

class TalkAdmin(admin.ModelAdmin):
    fields = (('title'),('members','date'),'topics')
    select2 = select2_modelform(Talk, attrs={'width': '250px'})
    form = select2

admin.site.register(Project, ProjectAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Honour, HonourAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Talk, TalkAdmin)