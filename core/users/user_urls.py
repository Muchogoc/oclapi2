from django.urls import re_path, include

from core.common.constants import NAMESPACE_PATTERN
from core.orgs import views as orgs_views
from core.repos.views import OrganizationRepoListView
from core.url_registry.views import OrganizationURLRegistryListView
from core.users import views

extra_kwargs = {'user_is_self': True}

# shortcuts for the currently logged-in user
urlpatterns = [
    re_path(
        r'^$', views.UserDetailView.as_view(), extra_kwargs, name='user-self-detail'
    ),
    re_path(
        r'^orgs/$', orgs_views.OrganizationListView.as_view(), extra_kwargs, name='user-organization-list'
    ),
    re_path(
        r'^extras/$',
        views.UserExtrasView.as_view(),
        extra_kwargs,
        name='user-extras'
    ),
    re_path(
        r'^orgs/sources/$',
        orgs_views.OrganizationSourceListView.as_view(),
        extra_kwargs,
        name='user-organization-source-list'
    ),
    re_path(
        r'^orgs/collections/$',
        orgs_views.OrganizationCollectionListView.as_view(),
        extra_kwargs,
        name='user-organization-collection-list'
    ),
    re_path(
        r'^orgs/repos/$',
        OrganizationRepoListView.as_view(),
        extra_kwargs,
        name='user-organization-repo-list',
    ),
    re_path(
        r'^orgs/url-registry/$',
        OrganizationURLRegistryListView.as_view(),
        extra_kwargs,
        name='user-organization-url-registry-list',
    ),
    re_path(
        fr"^extras/(?P<extra>{NAMESPACE_PATTERN})/$",
        views.UserExtraRetrieveUpdateDestroyView.as_view(),
        extra_kwargs,
        name='user-extra'
    ),
    re_path(r'^sources/', include('core.sources.urls'), extra_kwargs),
    re_path(r'^collections/', include('core.collections.urls'), extra_kwargs),
    re_path(r'^repos/', include('core.repos.urls'), extra_kwargs),
    re_path(r'^url-registry/', include('core.url_registry.urls'), extra_kwargs),
    re_path(r'^pins/', include('core.pins.urls'), extra_kwargs)
]
