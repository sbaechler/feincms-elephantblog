.. _extensions:


Pinging
-------

The Pinging app uses the management command manage.py blogping to generate the
pings for the search engines. Set it up to run as a cron job.

You need to add the following statements to your settings file::

    BLOG_TITLE = 'My great blog'
    BLOG_BASE_URL = 'http://mysite.com/blog/'

Then register the extension. In yourapp.models.py::

    Entry.register_extensions('blogping',)

Add `pinging` to your `settings.INSTALLED_APPS`.

Here is a list of servers that can be used for pinging:
`<http://www.webpage-designer.net/65-wordpress-pinging-urls-you-need-to-know/>`_


Template
--------

While the Entry model supports ``register_templates``, the selector is not added
to the admin. Therefore you need to add the ``elephantblog.extensions.templates``
extension. Keep in mind that only the detail view supports multiple templates
and that you have to set the full path to the entry_detail.html. Use the ``key``
attribute if the path is to long:

  Entry.register_templates({
      'title': 'News',
      'key': 'entry',
      'path': 'elephantblog/entry_detail.html',
      'regions': (
          ('main', _('Main content area')),
          ('sidebar', _('Sidebar right')),
      ),
  },
  ...)