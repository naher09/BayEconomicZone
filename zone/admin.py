from django.contrib import admin
from django.utils.html import format_html
from .models import *


# -------------------------------
# HomeBanner Admin
# -------------------------------
@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('sequence', 'title', 'subtitle', 'is_active', 'created_at', 'banner_preview')
    list_editable = ('sequence', 'is_active')
    list_display_links = ('title',)   # ✅ FIX
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
    readonly_fields = ('banner_preview', 'created_at')
    ordering = ('sequence',)

    def banner_preview(self, obj):
        if obj.background_image:
            return format_html(
                '<img src="{}" style="height: 60px; width:auto; border-radius:5px;" />',
                obj.background_image.url
            )
        return "-"
    banner_preview.short_description = 'Preview'



# -------------------------------
# HomeAboutSection Admin
# -------------------------------
@admin.register(HomeAboutSection)
class HomeAboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'image_1_preview', 'image_2_preview')
    list_filter = ('is_active',)
    search_fields = ('title',)
    readonly_fields = ('image_1_preview', 'image_2_preview', 'created_at')
    ordering = ('-created_at',)

    def image_1_preview(self, obj):
        if obj.image_1:
            return format_html(
                '<img src="{}" style="height: 60px; width:auto; border-radius:5px;" />',
                obj.image_1.url
            )
        return "-"
    image_1_preview.short_description = 'Image 1'

    def image_2_preview(self, obj):
        if obj.image_2:
            return format_html(
                '<img src="{}" style="height: 60px; width:auto; border-radius:5px;" />',
                obj.image_2.url
            )
        return "-"
    image_2_preview.short_description = 'Image 2'


@admin.register(WhyChooseUsSection)
class WhyChooseUsSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active', 'created_at')  # Columns to display
    list_filter = ('is_active', 'created_at')  # Filters in the sidebar
    search_fields = ('title', 'subtitle', 'description') # Searchable fields
    readonly_fields = ('created_at',)  # Read-only fields

@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

@admin.register(HomeProject)
class HomeProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at',)

@admin.register(HomeBlockPost)
class HomeBlockPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
        ('Button & Status', {
            'fields': ('button_link', 'is_active')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Image'

@admin.register(HomeOutPartner)
class HomeOutPartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'image_preview')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:50%;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = 'Image'

@admin.register(AboutPageHeader)
class PageHeaderAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'page_title', 'is_active')  # <-- title পরিবর্তন করে page_title
    list_editable = ('is_active',)
    search_fields = ('page_name', 'page_title')


@admin.register(ComplianceSection)
class ComplianceSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_editable = ('is_active',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Compliance Information', {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

# ------------------------------
# Key Management Admin
# ------------------------------

# -------------------------------
# Key Management Headline Admin
# -------------------------------

# -------------------------------
# Key Management Member Admin
# -------------------------------
@admin.register(KeyManagement)
class KeyManagementAdmin(admin.ModelAdmin):
    list_display = (
        'image_preview',
        'name',
        'designation',
        'order',
        'is_active',
    )

    list_filter = ('is_active',)
    search_fields = ('name', 'designation')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:5px;" />',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Image"

    def get_short_designation(self, obj):
        return obj.designation[:50] + "..." if len(obj.designation) > 50 else obj.designation
    get_short_designation.short_description = "Designation"

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_editable = ('is_active',)

    fieldsets = (
        ('About Information', {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    readonly_fields = ('created_at',)

    def preview_image_1(self, obj):
        if obj.image_1:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:4px;" />',
                obj.image_1.url
            )
        return "No Image"

    preview_image_1.short_description = "Image 1"

    def preview_image_2(self, obj):
        if obj.image_2:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:4px;" />',
                obj.image_2.url
            )
        return "No Image"

    preview_image_2.short_description = "Image 2"


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)


@admin.register(LegalFramework)
class LegalFrameworkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'description',
    )

    list_editable = (
        'is_active',
    )

    ordering = ('-id',)

    fieldsets = (
        ('Legal Framework Information', {
            'fields': (
                'title',
                'description',
                'important_link',
                'image',
            )
        }),
        ('Status', {
            'fields': (
                'is_active',
            )
        }),
    )


@admin.register(FacilitiesIncentives)
class FacilitiesIncentivesAdmin(admin.ModelAdmin):
    list_display = (
        'short_title',
        'title',
        'is_active',
    )

    list_editable = (
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'short_title',
        'title',
        'description',
    )

    ordering = ('-id',)

    fieldsets = (
        ('Facilities & Incentives Content', {
            'fields': (
                'short_title',
                'title',
                'description',
            )
        }),
        ('Status', {
            'fields': (
                'is_active',
            )
        }),
    )

@admin.register(OurGallery)
class OurGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'image_tag')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('is_active',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:auto; border-radius:5px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


# NewsEvents hidden for now

# -------------------------------
# Admin for RequestInvestorData
# -------------------------------
@admin.register(RequestInvestorData)
class RequestInvestorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_title')
    search_fields = ('short_title',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('short_title', 'image')
        }),
    )

# -------------------------------
# Admin for RequestInvestorMessage
# -------------------------------
@admin.register(RequestInvestorMessage)
class RequestInvestorMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'city', 'country', 'created_at', 'is_read')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'phone', 'city', 'country')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'phone', 'city', 'country', 'address', 'message', 'created_at')

    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'phone', 'city', 'country', 'address', 'created_at')
        }),
        ('Message', {
            'fields': ('message', 'is_read')
        }),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'phone_number', 'email_address', 'office_address','map_link', 'is_active')
    list_editable = ('map_link', 'is_active',)
    search_fields = ('title', 'phone_number', 'email_address', 'office_address')
    list_filter = ('is_active',)
    fieldsets = (
        ('General Info', {
            'fields': ('title', 'description', 'is_active')
        }),
        ('Contact Details', {
            'fields': ('phone_number', 'email_address', 'office_address', 'map_link')
        }),
    )


# -------------------------------
# Admin for ContactMessage
# -------------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_at', 'is_read')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'created_at')
        }),
        ('Message', {
            'fields': ('subject', 'message', 'is_read')
        }),
    )

@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = (
        'short_title',
        'title',
        'is_active',
        'image_preview',
    )

    list_filter = ('is_active',)
    search_fields = ('short_title', 'title')
    list_editable = ('is_active',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('short_title', 'title', 'is_active')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('Images', {
            'fields': ('image_1', 'image_preview')
        }),
    )

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image_1:
            return format_html(
                '<img src="{}" style="height:80px; border-radius:6px;" />',
                obj.image_1.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


# -------------------------------
# Site Banner Admin (page-specific header banner, all pages except home)
# -------------------------------
@admin.register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'image_preview', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('page_name', 'page_title')
    readonly_fields = ('image_preview', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('page_name', 'page_title', 'image', 'link', 'is_active')
        }),
        ('Preview', {
            'fields': ('image_preview', 'created_at')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; border-radius:5px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = 'Preview'