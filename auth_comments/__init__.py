from django.core import urlresolvers

def get_form_target():
    return urlresolvers.reverse("auth_comments.views.comment_submit_wrapper")
