from django.contrib import admin
from .models import Feedback
from .models import FeedbackCategory

admin.site.register(Feedback)
admin.site.register(FeedbackCategory)