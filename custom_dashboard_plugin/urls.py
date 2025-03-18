from django.urls import re_path
from custom_dashboard_plugin import views

urlpatterns = [
    re_path(r'^$', views.CommitPanelView.as_view(), name='index'),
]
