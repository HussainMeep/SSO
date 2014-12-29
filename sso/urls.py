from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp.views import IndexView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    url(r'^$', login_required(IndexView.as_view()), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r"^accounts/", include("account.urls")),
)
