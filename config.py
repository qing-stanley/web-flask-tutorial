import os


# get base directory
basedir = os.path.abspath(os.path.dirname(__file__))


# set database info
# path of database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# directory of sqlalchemy-migrate data file
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# track modifications of objects and emit signals
SQLALCHEMY_TRACK_MODIFICATIONS = True


# enable form
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
# set openid providers
OPENID_PROVIDERS = [
    {'name': 'Google',
     'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo',
     'url': 'https://me.yahoo.com'},
    {'name': 'AOL',
     'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr',
     'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID',
     'url': 'https://www.myopenid.com'}]




