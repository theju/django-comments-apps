"""
Change the attributes that you want to customize.
"""

from recaptcha_comments.forms import RecaptchaCommentForm
from django.core import urlresolvers

def get_form():
    return RecaptchaCommentForm

def get_form_target():
    return urlresolvers.reverse("recaptcha_comments.views.validate_and_submit")
