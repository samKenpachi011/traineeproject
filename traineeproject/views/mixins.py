from django.apps import apps as django_apps

# return a context with urls for listboards for all apps

class AppConfigListboardUrlsViewMixin:

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update(
            dashboard_url_name=django_apps.get_app_config(
                self.dashboard_url_app_label).dashboard_url_name,)
        return context