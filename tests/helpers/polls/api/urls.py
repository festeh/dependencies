from django.conf.urls import url

from .views import (
    BadNegotiation,
    LoginAll,
    ThrottleAll,
    UserAction,
    UserListView,
    UserLogin,
    UserRetrieveView,
)

urlpatterns = [
    url(r"^action/$", UserAction.as_view(), name="api-action"),
    url(r"^login/$", UserLogin.as_view(), name="api-login"),
    url(r"^login_all/$", LoginAll.as_view(), name="api-login-all"),
    url(r"^throttle_all/$", ThrottleAll.as_view(), name="api-throttle-all"),
    url(r"^negotiate/$", BadNegotiation.as_view(), name="api-negotiate"),
    url(r"^users/$", UserListView.as_view(), name="api-user-list"),
    url(r"^users/(?P<nick>\w+)/$", UserRetrieveView.as_view(), name="api-user-detail"),
]
