from django.conf.urls import url
# from django.contrib import admin
import blog.views 

urlpatterns = [

	url(r'^blogs',blog.views.blogs,name='blogs_url'),
	url(r'^blogadd',blog.views.blogadd,name='blogadd_url'),
	url(r'^blogedit',blog.views.blogedit,name='blogedit_url'),

		
]