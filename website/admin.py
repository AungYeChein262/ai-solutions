from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "company_name",
        "country",
        "job_title",
        "date_submitted",
    )
    search_fields = ("name", "email", "company_name")
    list_filter = ("country", "date_submitted")
    ordering = ("-date_submitted",)

from django.contrib import admin
from .models import Feedback

from django.contrib import admin
from .models import Feedback

admin.site.site_header = "AI-Solutions Administration"
admin.site.site_title = "AI-Solutions Admin"
admin.site.index_title = "Admin Dashboard"

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "job_title", "rating", "submitted_at")
    list_filter = ("rating", "submitted_at")
    search_fields = ("name", "company", "job_title", "message")


from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
