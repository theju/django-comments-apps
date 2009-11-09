========
INSTALL
========

* Reference the app (``auth_comments``) under the ``INSTALLED_APPS`` in ``settings.py``
* Add the ``COMMENTS_APP`` attribute in ``settings.py`` and set the value to ``auth_comments``
* Make sure that you have the following ``TEMPLATE_CONTEXT_PROCESSORS`` activated in your ``settings.py``::

    TEMPLATE_CONTEXT_PROCESSORS=(
      "django.core.context_processors.auth",
      "django.core.context_processors.request",
      "django.core.context_processors.media"
    )

* Append the auth_comments/templates directory in the ``TEMPLATE_DIRS`` attribute of ``settings.py``
* Activate the comment urls in your project's urls.py::

    (r'^comment/', include('django.contrib.comments.urls')),

* Add the ``ReRenderMiddleware`` to the ``MIDDLEWARE_CLASSES`` in ``settings.py``::

    MIDDLEWARE_CLASSES = (
    ...
    'recaptcha_comments.middleware.ReRenderMiddleware',
    )

* In your templates, when you want to render the authenticated comment form, just use the following code::

    {% load auth_comments %}
    ...
    {% render_auth_comment_form for app.model object_pk %}

  This code is equivalent to::

    {% if request.user.is_authenticated %}
      {% render_comment_form for app.model object_pk %}
    {% else %}
      <!-- Some standard message to be shown if user not logged in. -->
    {% endif %}

* The standard message is picked up from the ``DEFAULT_UNAUTH_COMMENT_MESSAGE`` attribute of ``settings.py`` which you can set to override the default message.