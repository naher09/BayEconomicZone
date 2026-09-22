from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# @@@@@ Home Models @@@@@@@@@@

class HomeBanner(models.Model):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    background_image = models.ImageField(upload_to='Carousel/', blank=True, null=True)
    button_text = models.CharField(max_length=100, default='Our Services', blank=True, null=True)
    button_link = models.URLField(max_length=300, default='#', blank=True, null=True)

    sequence = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class HomeAboutSection(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image_1 = models.ImageField(upload_to='About/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='About/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class WhyChooseUsSection(models.Model):
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image = models.ImageField(upload_to='why_choose_us/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeService(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeProject(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeBlockPost(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title

class HomeOutPartner(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image = models.ImageField(upload_to='partners/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title


class AboutPageHeader(models.Model):
    page_name = models.CharField(max_length=100, blank=True, null=True)
    page_title = models.CharField(max_length=200, blank=True, null=True)
    background_image = models.ImageField(upload_to='page_headers/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.page_name

class AboutSection(models.Model):
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market")
    description = RichTextUploadingField('Description')
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class ComplianceSection(models.Model):
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market")
    description = RichTextUploadingField('Description')
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class KeyManagement(models.Model):
    """Model to represent a key management or advisory team member."""
    image = models.ImageField(upload_to='key_management/')
    name = models.CharField(max_length=200)
    designation = RichTextUploadingField('Description')
    description = RichTextUploadingField('Description')
    link = models.URLField()
    order = models.PositiveIntegerField(default=0, help_text="Controls display order on the page.")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide this person from the website.")

    def __str__(self):
        return self.name

class LegalFramework(models.Model):
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    important_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='legal_framework/', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title

class FacilitiesIncentives(models.Model):
    short_title = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title

class OurService(models.Model):
    short_title = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image_1 = models.ImageField(upload_to='service_image_1/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='service_image_2/', blank=True, null=True)

    order = models.PositiveIntegerField(default=0, help_text="Controls display order")

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']   # 🔥 default ordering

    def __str__(self):
        return self.title

class Mission(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Vision(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class OurGallery(models.Model):
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    image = models.ImageField(upload_to='gallery', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title

class NewsEvents(models.Model):
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image = models.ImageField(upload_to='news_events_image/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title

class RequestInvestorData(models.Model):
    short_title = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    image = models.ImageField(upload_to='investor/', blank=True, null=True)

    class Meta:
        verbose_name = "Register as Investor"
        verbose_name_plural = "Register as Investors"

    def __str__(self):
        return self.title

class RequestInvestorMessage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Automatically set timestamp

    is_read = models.BooleanField(default=False, blank=True, null=True)  # Optional: mark if admin has read

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Register as Investor Message"
        verbose_name_plural = "Register as Investor Messages"


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    office_address = models.CharField(max_length=300, default="We Are Leader", blank=True, null=True)
    map_link = models.URLField(blank=True, null=True, max_length=500)
    title = models.CharField(max_length=300, default="We Are Leader In Industrial Market", blank=True, null=True)
    description = RichTextUploadingField('Description', blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Automatically set timestamp

    is_read = models.BooleanField(default=False, blank=True, null=True)  # Optional: mark if admin has read

    def __str__(self):
        return f"{self.name} - {self.email}"


class SiteBanner(models.Model):
    """Admin-managed page header title. One per page (all pages except home)."""
    page_name = models.CharField(
        max_length=50, blank=True, null=True,
        help_text="URL slug, e.g. about, compliance, contact. Leave blank to apply to all pages."
    )
    page_title = models.CharField(max_length=200, blank=True, null=True, help_text="Optional page title override")
    image = models.ImageField(upload_to='site_banner/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page_name or "Site Banner"

    class Meta:
        verbose_name = "Site Banner"
        verbose_name_plural = "Site Banner"
