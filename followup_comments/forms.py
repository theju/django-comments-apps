from django import forms
from followup_comments.models import FollowUpComment
from django.contrib.comments.forms import CommentForm

class FollowUpCommentForm(CommentForm):
    need_follow_up = forms.BooleanField(initial=False, required=False)

    def get_comment_model(self):
        return FollowUpComment

    def get_comment_create_data(self):
        dict = super(FollowUpCommentForm, self).get_comment_create_data()
        dict.update({"need_follow_up": self.cleaned_data["need_follow_up"]})
        return dict
