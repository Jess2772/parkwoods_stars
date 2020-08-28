""" Define URL patterns for parkwoods_app"""

from django.urls import path

from . import views
app_name = 'parkwoods_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for rosters
    path('rosters/', views.rosters, name='rosters'),
    # Page for awards
    path('awards/', views.awards, name='awards'),
    # Page for videos
    path('videos/', views.videos, name='videos'),
    # Page for standings
    path('standings/', views.standings, name='standings'),
    # Page for playoff standings
    path('standings_playoff/', views.standings_playoff, name='standings_playoff'),
    # Page for semi-finals standings
    path('standings_semi/', views.standings_semi, name='standings_semi'),
    # Page for finals standings
    path('standings_finals/', views.standings_finals, name='standings_finals'),
    # Page for schedule
    path('schedule/', views.schedule, name='schedule'),
    # Page for playoff schedule
    path('schedule_playoff/', views.schedule_playoff, name='schedule_playoff'),
    # Page for semi-finals schedule
    path('schedule_semi/', views.schedule_semi, name='schedule_semi'),
    # Page for finals schedule
    path('schedule_finals/', views.schedule_finals, name='schedule_finals'),    
    
    # Page for about me
    path('aboutme/', views.aboutme, name='aboutme'),
]
