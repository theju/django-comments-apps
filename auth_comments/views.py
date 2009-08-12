from django.contrib.comments.views.comments import post_comment, CommentPostBadRequest

def comment_submit_wrapper(request):
    # Clean the request to prevent form spoofing
    name_entered  = request.POST.get('name')
    email_entered = request.POST.get('email')

    if request.user.is_authenticated():
        if name_entered and not request.user.get_full_name() == name_entered:
            return CommentPostBadRequest("An attempt to spoof the comment form by "
                                         "supplying a wrong name was detected.")
        if email_entered and not request.user.email == email_entered:
            return CommentPostBadRequest("An attempt to spoof the comment form by "
                                         "supplying a wrong email was detected.")
        return post_comment(request)
    return CommentPostBadRequest("Only authenticated users are allowed to post comments.")

