"""
API views not coupled to models.
"""
from django.core.urlresolvers import reverse

from djangorestframework.views import View


class RootView(View):
    """
    Startpoint.
    """
    def get(self, request):
         return {
            "categories": reverse(
                'lizard_wbconfiguration_api_area_configuration_root'),
            }