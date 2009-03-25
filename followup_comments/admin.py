from django.contrib import admin
from django.contrib.comments.admin import CommentsAdmin
from django.utils.translation import ugettext_lazy as _
from followup_comments.models import FollowUpComment, FollowUpMessage

class FollowUpCommentsAdmin(CommentsAdmin):
    fieldsets = (
        (None,
           {'fields': ('content_type', 'object_pk', 'site')}
        ),
        (_('Content'),
           {'fields': ('user', 'user_name', 'user_email', 'user_url', 'comment')}
        ),
        (_('Metadata'),
           {'fields': ('submit_date', 'ip_address', 'is_public', 'is_removed', 'need_follow_up')}
        ),
     )

    list_display = ('name', 'content_type', 'object_pk', 'ip_address', 'submit_date', 'is_public', 'is_removed', 'need_follow_up')
    list_filter = ('submit_date', 'site', 'is_public', 'is_removed', 'need_follow_up',)


class FollowUpMessageAdmin(admin.ModelAdmin):
    list_display = ('site', 'message')


admin.site.register(FollowUpMessage, FollowUpMessageAdmin)
admin.site.register(FollowUpComment, FollowUpCommentsAdmin)
