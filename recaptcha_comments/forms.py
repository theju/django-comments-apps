from django.contrib.comments.forms import CommentForm
from recaptcha_comments.fields import RecaptchaField

class RecaptchaCommentForm(CommentForm):
    captcha = RecaptchaField()

    def clean_captcha(self):
        if not 'preview' in self.data:
            captcha_data = self.cleaned_data['captcha']
            return self.fields['captcha'].verify(captcha_data)
