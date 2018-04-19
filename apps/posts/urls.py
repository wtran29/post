from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^posts$', views.dashboard),
	url(r'^posts/create$', views.create_post),
	url(r'^posts/delete$', views.delete),
	url(r'^posts/post.html$', views.post_html),
	url(r'^posts/edit$', views.edit),
	# url(r'^posts/edit.html$', views.edit),
	# url(r'^posts/update/(?P<number>\d+)$', views.update),
]