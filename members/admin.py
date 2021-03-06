from django.contrib import admin
from .models import *
from activity.models import *
from .inlines import *
from easy_select2 import select2_modelform

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Details', {
            'fields': (('user', 'role'), ('email', 'phone'),
                       ('first_name', 'last_name'), ('roll_number', 'batch'))
        }),
        ('Additional Details', {
            'fields': (('avatar', 'birthday'),('resume','system_no'), ('location', 'languages'), 'tagline', 'about')
        }),
        ('Interests & Expertise', {
            'fields': (('interests', 'expertise'),)
        }),

    )
    inlines = (sp_inline, wexp_inline, eq_inline)
    list_display = ('first_name', 'last_name', 'role', 'batch')
    list_filter = ('batch','role')
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'batch', 'role']
    select2 = select2_modelform(Profile, attrs={'width': '250px'})
    form = select2

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    fields  = ('member',('session_start', 'session_end'),)
    list_display = ('member', 'session_start', 'session_end', 'duration')
    list_filter = ('member','session_start')
    select2 = select2_modelform(Attendance, attrs={'width': '250px'})
    form = select2



@admin.register(LeaveRecord)
class LeaveRecordAdmin(admin.ModelAdmin):
    fields= (('user','type'),('start_date','end_date'),'reason')
    list_display = ('user', 'type', 'start_date', 'end_date')
    list_filter = ('user','type')
    select2 = select2_modelform(LeaveRecord, attrs={'width': '250px'})
    form = select2

@admin.register(Responsibility)
class ResponsibilityAdmin(admin.ModelAdmin):
    search_fields = ['title', 'members']
    list_display = ('title', 'thread')
    list_filter = ('title','members')
    select2 = select2_modelform(Responsibility, attrs={'width': '250px'})
    form = select2

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name', 'members']
    list_display = ('name', 'thread')
    list_filter = ('name', 'members')
    select2 = select2_modelform(Team, attrs={'width': '250px'})
    form = select2

@admin.register(MentorGroup)
class MentorGroupAdmin(admin.ModelAdmin):
    search_fields = ['mentor', 'mentees']
    list_display = ('mentor',)
    list_filter = ('mentor',)
    select2 = select2_modelform(MentorGroup, attrs={'width': '250px'})
    form = select2

@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
