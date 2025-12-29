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
            "country",
            "job_title",
            "job_details",
        ]

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "job_title", "company", "rating", "message"]

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "job_title", "company", "rating", "message"]

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating is None or rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating