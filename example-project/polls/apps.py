from django.apps import AppConfig

# Version History:
#   2020.12.30.100 
#   Finished part three of tutorial.  https://docs.djangoproject.com/en/3.1/intro/tutorial03
#   
#   2020.01.07.BeforeGenericViews 
#   Added vote and results views.  From here migrating to generic views.  https://docs.djangoproject.com/en/3.1/intro/tutorial04/#use-generic-views-less-code-is-better
#   
#   2020.01.07.AfterGenericViews 
#   Removed specific view definitions and replaced with generic views provided by Django.
#

class PollsConfig(AppConfig):
    name = 'polls'
