"""
Change the attributes you want to customize
"""

from threaded_comments.models import ThreadedComment
from threaded_comments.forms import ThreadedCommentForm

def get_model():
    return ThreadedComment

def get_form():
    return ThreadedCommentForm
