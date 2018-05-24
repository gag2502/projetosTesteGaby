from django.conf.urls import url
from .views import LoginView, TesteView
from .views import AuthorCreate, AuthorUpdate, AuthorDelete, AuthorDetailView


urlpatterns = [
    url(r'^$', LoginView.as_view(),
        name='login'),
    url(r'^login/$', LoginView.as_view(),
        name='login'),
    url(r'^teste/', TesteView.as_view(),
        name='teste'),
    url(r'author/add/$', AuthorCreate.as_view(),name='author_add'),
    url(r'author/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author_update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
    #url(r'^(?P<slug>[-_\w]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/(?P<pk>[0-9]+)/detail/$', AuthorDetailView.as_view(), name='author-detail'),
]
