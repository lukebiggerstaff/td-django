from django.conf.urls import url
from accounts import views as accounts_views
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^send_login_email$', accounts_views.send_login_email,name='send_login_email'),
    url(r'^login$', accounts_views.login,name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
