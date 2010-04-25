from django.contrib.comments.forms import CommentForm
from recaptcha_comments.fields import RecaptchaField

class RecaptchaCommentForm(CommentForm):
    captcha = RecaptchaField()

    def clean_captcha(self):
        self.fields['captcha'].verify(self.cleaned_data['captcha'])
        return self.cleaned_data['captcha']
