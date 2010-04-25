from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
import urllib2, urllib

VERIFY_SERVER="http://api-verify.recaptcha.net/verify"

class RecaptchaWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return mark_safe("""<script type="text/javascript" 
                          src="http://api.recaptcha.net/challenge?k=%(public_key)s"></script>
                  <noscript>
                     <iframe src="http://api.recaptcha.net/noscript?k=%(public_key)s"
                             height="300" width="500" frameborder="0"></iframe><br>
                     <textarea name="recaptcha_challenge_field" rows="3" cols="40">
                     </textarea>
                     <input type="hidden" name="recaptcha_response_field" value="manual_challenge">
                  </noscript>""" %({'public_key': settings.RECAPTCHA_PUBLIC_KEY}))

    def value_from_datadict(self, data, files, name):
        return {
            'recaptcha_challenge_field': data.get('recaptcha_challenge_field', None),
            'recaptcha_response_field' : data.get('recaptcha_response_field', None),
            'remoteip' : data.get('remoteip', None)
        }

class RecaptchaField(forms.Field):
    default_error_messages = {"unknown": _("Unknown error."),
                              "invalid-site-public-key": _("Unable to verify public key."),
                              "invalid-site-private-key": _("Unable to verify private key."),
                              "invalid-request-cookie": _("The challenge parameter was filled incorrectly."),
                              "incorrect-captcha-sol": _("Invalid Captcha solution."),
                              "verify-params-incorrect": _("Make sure you are passing all the required parameters."),
                              "invalid-referrer": _("Invalid Referrer. Enter the correct keys for this domain"),
                              "recaptcha-not-reachable": _("The reCaptcha site seems to be down. Sorry!!!")}
    widget = RecaptchaWidget

    def verify(self, data):
        captcha_req = urllib2.Request(VERIFY_SERVER,
                                      data=urllib.urlencode({'privatekey': settings.RECAPTCHA_PRIVATE_KEY,
                                                             'remoteip'  : data['remoteip'],
                                                             'challenge' : data['recaptcha_challenge_field'],
                                                             'response'  : data['recaptcha_response_field'],}))
        try:
            response = urllib2.urlopen(captcha_req)
        except urllib2.URLError,e :
            raise forms.ValidationError(e)
        resp_content = response.readlines()
        return_code = resp_content[0].strip()
        error = resp_content[1].strip()
        if not return_code == "true":
            raise forms.ValidationError(self.error_messages.get(error) or error)
