from django.urls import path
from custom_dashboard_plugin.views import WikiView

urlpatterns = [
    path('', WikiView.as_view(), name='wiki_index'),
]