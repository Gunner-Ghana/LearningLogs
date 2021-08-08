"""Define url paths used for learning_logs"""
from django.urls import path,re_path
from . import views

urlpatterns = [
				#home page
				path('',views.index, name='index'),
				
				#show topics
				path('topics/', views.topics, name='topics'),
				
				#detail in topic
				re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
				
				#page for adding a new topic
				path('new_topic/', views.new_topic, name='new_topic'),
				
				#page for adding a new entry
				re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
				
				re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry')
				
				]

app_name = 'learning_logs'
