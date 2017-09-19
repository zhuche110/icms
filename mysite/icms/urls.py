from django.conf.urls import url
from django.conf.urls import url,include
from django.contrib import admin
import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
	url(r'view/(?P<entries_id>[0-9]+)',views.entries_views),
	url(r'cat/page/(?P<page_num>[0-9]+)/',views.category_views),
url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
