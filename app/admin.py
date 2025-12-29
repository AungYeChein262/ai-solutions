from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "date_submitted")
    list_filter = ("date_submitted",)
    search_fields = ("name", "email", "company")
