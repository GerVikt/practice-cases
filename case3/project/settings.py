
SECRET_KEY = 'testkey'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = ['app']

MIDDLEWARE = ['django.middleware.csrf.CsrfViewMiddleware']

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['app/templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': []},
    },
]

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': 'db.sqlite3'}}
