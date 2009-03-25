from followup_comments.models import FollowUpComment
from followup_comments.forms import FollowUpCommentForm

def get_model():
    return FollowUpComment

def get_form():
    return FollowUpCommentForm
