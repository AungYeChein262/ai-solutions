from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            "name",
            "email",
            "phone",
            "company_name",
            "job_title",
            "country",
            "job_details",
        ]


from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "job_title", "company", "rating", "message"]
