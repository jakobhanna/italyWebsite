AUTHOR = 'moriati'
SITENAME = '* Istrice *'
SITESUBTITLE = 'CPM+SO'
SITEURL = ''
THEME = 'solar'

PATH = 'content'
PLUGIN_PATHS = ["plugins", "plugin/solar-plugins/"]
PLUGINS = ["addressable_paragraphs", "assets", "dither", "page_metadata", "related_posts", "representative_image", "thumbnailer"]

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'de'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'startinline': True},
    },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/jakobhanna/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True