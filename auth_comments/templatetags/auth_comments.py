import settings
from django import template
from django.contrib.comments.templatetags.comments import BaseCommentNode, CommentFormNode

register = template.Library()

DEFAULT_UNAUTH_COMMENT_MESSAGE = getattr(settings, 'DEFAULT_UNAUTH_COMMENT_MESSAGE', None) or \
                                 """<p>Please register/sign-in to post comments.<p>"""

class RenderAuthCommentFormNode(CommentFormNode):
    """Render the comment form directly"""

    #@classmethod
    def handle_token(cls, parser, token):
        """Class method to parse render_comment_form and return a Node."""
        tokens = token.contents.split()
        if tokens[1] != 'for':
            raise template.TemplateSyntaxError("Second argument in %r tag must be 'for'" % tokens[0])

        # {% render_comment_form for obj %}
        if len(tokens) == 3:
            return cls(object_expr=parser.compile_filter(tokens[2]))

        # {% render_comment_form for app.models pk %}
        elif len(tokens) == 4:
            return cls(
                ctype = BaseCommentNode.lookup_content_type(tokens[2], tokens[0]),
                object_pk_expr = parser.compile_filter(tokens[3])
            )
    handle_token = classmethod(handle_token)

    def render(self, context):
        ctype, object_pk = self.get_target_ctype_pk(context)
        if object_pk:
            return """{%% load comments %%}
                      {%% if request.user.is_authenticated %%}
                        {%% render_comment_form for %s.%s %d %%}
                      {%% else %%}
                        %s
                      {%% endif %%}""" %(ctype.app_label, ctype.model, 
                                         object_pk, DEFAULT_UNAUTH_COMMENT_MESSAGE)
        else:
            return ''

def render_auth_comment_form(parser, token):
    """
    Syntax::

        {% render_auth_comment_form for [object] %}
        {% render_auth_comment_form for [app].[model] [object_id] %}

        is equivalent to

        {% if request.user.is_authenticated %}
          {% render_comment_form for [app].[model] [object_id] %}
        {% else %}
          <p>Please register/log-in to post comments.</p>
        {% endif %}
    """
    return RenderAuthCommentFormNode.handle_token(parser, token)

register.tag(render_auth_comment_form)
