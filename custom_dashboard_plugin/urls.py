from django.conf.urls import url
from custom_dashboard_plugin import views

urlpatterns = [
    url(r'^$', views.CommitPanelView.as_view(), name='index'),
]