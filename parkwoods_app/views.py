from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime

from .models import Topic, Entry, Standings, Schedule
from .forms import TopicForm, EntryForm


def index(request):
    """The home page."""
    return render(request, 'parkwoods_app/index.html')


def rosters(request):
    """The rosters page."""
    return render(request, 'parkwoods_app/rosters.html')

def awards(request):
    """The awards page."""
    return render(request, 'parkwoods_app/awards.html')


def videos(request):
    """The video page."""
    return render(request, 'parkwoods_app/videos.html')


def standings(request):
    """Show all standings."""    
    standings = Standings.objects.filter(season='WY20').order_by('-pts', '-wins', '-gfavg')
    context = {'standings': standings}
    return render(request, 'parkwoods_app/standings.html', context)
    
def standings_playoff(request):
    """Show all standings."""
    standings = Standings.objects.filter(pl_group='G1').order_by('-pts', '-wins', '-gfavg')
    groupB = Standings.objects.filter(pl_group='G2').order_by('-pts', '-wins', '-gfavg')
    context = {'standings': standings, 'groupB': groupB}
    return render(request, 'parkwoods_app/standings_playoff.html', context)
    
def standings_semi(request):
    """Show all standings."""
    standings = Standings.objects.filter(season='SF20').order_by('-pts', '-wins', '-gfavg')
    context = {'standings': standings}
    return render(request, 'parkwoods_app/standings_semi.html', context)
    
def standings_finals(request):
    """Show all standings."""
    standings = Standings.objects.filter(season='FN20').order_by('-pts', '-wins', '-gfavg')
    context = {'standings': standings}
    return render(request, 'parkwoods_app/standings_finals.html', context)

def schedule(request):
    """The schedule page."""
    schedule = Schedule.objects.filter(season='WY20').order_by('game_dt', 'game_time')    
    context = {'schedule': schedule}
    return render(request, 'parkwoods_app/schedule.html', context)
    
def schedule_playoff(request):
    """The schedule page."""
    schedule = Schedule.objects.filter(season='PL20').order_by('game_dt', 'game_time')    
    context = {'schedule': schedule}
    return render(request, 'parkwoods_app/schedule_playoff.html', context)
    
def schedule_semi(request):
    """The schedule page."""
    schedule = Schedule.objects.filter(season='SF20').order_by('game_dt', 'game_time')    
    context = {'schedule': schedule}
    return render(request, 'parkwoods_app/schedule_semi.html', context)
    
def schedule_finals(request):
    """The schedule page."""
    schedule = Schedule.objects.filter(season='FN20').order_by('game_dt', 'game_time')    
    context = {'schedule': schedule}
    return render(request, 'parkwoods_app/schedule_finals.html', context)


def aboutme(request):
    """The about me page for Learning Log."""
    return render(request, 'parkwoods_app/aboutme.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'parkwoods_app/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'parkwoods_app/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('parkwoods_app:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'parkwoods_app/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return redirect('parkwoods_app:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'parkwoods_app/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.date_added = datetime.datetime.now()
            new_entry.save()
            return redirect('parkwoods_app:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'parkwoods_app/edit_entry.html', context)
