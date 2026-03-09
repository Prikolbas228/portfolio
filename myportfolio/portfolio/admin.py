from django.contrib import admin
from .models import Project, ContactMessage,Certificate

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']  # Пока только эти поля
    # list_display = ['title', 'github_url', 'created']  # Закомментировать
    search_fields = ['title']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'date', 'credential_id']
    list_filter = ['issuer', 'date']
    search_fields = ['title', 'issuer']


admin.site.register(Certificate, CertificateAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)