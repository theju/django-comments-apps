from django.contrib.comments.views.comments import post_comment

def validate_and_submit(request, next=None):
    # The next three lines are slightly hackish but there's not
    # much that can be done if we have to pass the ip
    # address to recaptcha
    ip_address = request.META.get('REMOTE_ADDR', None)
    post_querydict = request.POST.copy()
    post_querydict.update({'remoteip': ip_address})
    request.POST = post_querydict
    return post_comment(request, next=next)
