========
INSTALL
========

* Add ``django.contrib.comments`` and ``threaded_comments`` to ``INSTALLED_APPS`` in ``settings.py``.
* Add the following attributes in the ``settings.py``::

    COMMENTS_APP = "threaded_comments"

* Make use of the new comment tags that are available to help with the threaded support::

    {# To order comments by date use order_by date #}
    {% get_comment_list for app.model object.pk as comment_list order_by thread %}

    {% render_comment_form for app.model object.pk with comment.id %}
    {# Alternatively use #}
    {% get_comment_form for app.model object.pk as form with parent_id %}
