from django import template
from django.utils.safestring import mark_safe
from django.contrib.comments import get_form_target

def escape_template_code(value):
    return value.replace('#','&#35;').replace('%','&#37;').replace('{','&#123;').replace('}','&#125;')

class ReRenderMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == get_form_target():
            data = request.POST.copy()
            for item in data:
                data[item] = mark_safe(escape_template_code(data[item]))
            request.POST = data

    def process_response(self, request, response):
        if response.status_code != 200 or not response['Content-Type'].startswith('text'):
            return response

        t = template.Template(response.content)
        response.content = t.render(template.RequestContext(request))
        return response
