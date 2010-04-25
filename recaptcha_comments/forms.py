from django.contrib.comments.forms import CommentForm
from recaptcha_comments.fields import RecaptchaField

class RecaptchaCommentForm(CommentForm):
    captcha = RecaptchaField()

    def clean_captcha(self):
        return self.fields['captcha'].verify(self.cleaned_data['captcha'])
