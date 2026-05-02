from django.contrib import admin
from .models import Service, Project, Testimonial, ContactMessage, SiteConfig


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_featured', 'order')
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')
    search_fields = ('title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'result_highlight', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'tech_stack')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_role', 'is_featured', 'order')
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    actions = ['mark_as_read']

    @admin.action(description="Mark selected messages as read")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    def has_add_permission(self, request):
        return False


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_headline', 'hero_subheading')
        }),
        ('About Page', {
            'fields': ('about_intro', 'about_mission', 'about_vision')
        }),
        ('Statistics', {
            'fields': ('stat_projects', 'stat_experience', 'stat_clients')
        }),
        ('Contact Info', {
            'fields': ('contact_email', 'contact_phone', 'whatsapp_number')
        }),
        ('Footer', {
            'fields': ('footer_text',)
        }),
        ('Social Links', {
            'fields': ('social_facebook', 'social_twitter', 'social_linkedin', 'social_github'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
