from django.db import models
from django.contrib.comments.models import Comment
from django.core.mail import send_mass_mail
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.comments.signals import comment_was_posted

class FollowUpComment(Comment):
    need_follow_up = models.BooleanField()


class FollowUpMessage(models.Model):
    site = models.OneToOneField(Site)
    message = models.TextField()

    def __unicode__(self):
        return "%s: %s..." %(self.site.name, self.message[:15])


def send_followup_email(sender, **kwargs):
    instance = kwargs['comment']
    follow_up_users = FollowUpComment.objects.filter(need_follow_up=True).values('user_email')
    site = Site.objects.get(id=settings.SITE_ID)
    subject = ("[%s] Follow up to comment posted "
               "for %s at %s" %(site.name, 
                                instance.content_object, 
                                site.domain))
    followup_message = FollowUpMessage.objects.get(site__id=settings.SITE_ID).message
    message = """%s\n\n%s by %s at %s""" %(followup_message,
                                           instance.comment,
                                           instance.user_name,
                                           instance.submit_date.strftime(settings.DATETIME_FORMAT))

    data_list = []
    for user in follow_up_users:
        data_list.append([subject, message, None, [user['user_email'],]])

    send_mass_mail(data_list)


comment_was_posted.connect(send_followup_email)
