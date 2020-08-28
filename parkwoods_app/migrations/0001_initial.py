# Generated by Django 3.1 on 2020-08-26 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_dt', models.DateField()),
                ('game_time', models.TimeField()),
                ('away', models.CharField(max_length=30)),
                ('home', models.CharField(max_length=30)),
                ('score', models.CharField(max_length=5)),
                ('venue', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('division', models.CharField(choices=[('TK', 'Tyke'), ('MN', 'Minor Novice'), ('NV', 'Novice'), ('MA', 'Minor Atom'), ('AT', 'Atom'), ('MP', 'Minor Peewee'), ('PW', 'Peewee'), ('MB', 'Minor Bantam'), ('BT', 'Bantam'), ('MM', 'Minor Midget'), ('MJ', 'Midget Junior'), ('MS', 'Midget Senior'), ('UD', 'Under 21')], default='MS', max_length=2)),
                ('season', models.CharField(choices=[('FN20', 'FINAL 2020'), ('SF20', 'SEMI-FINAL 2020'), ('PL20', 'Playoff 2020'), ('WY20', 'Winter Season 2020'), ('FY19', 'Fall Season 2019')], default='WY20', max_length=4)),
                ('level', models.CharField(choices=[('T1', 'Tier 1'), ('T2', 'Tier 2'), ('T3', 'Tier 3')], default='T1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gp', models.IntegerField(default=0, editable=False)),
                ('pts', models.IntegerField(default=0, editable=False)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('ties', models.IntegerField(default=0)),
                ('gf', models.IntegerField(default=0)),
                ('ga', models.IntegerField(default=0)),
                ('gfavg', models.DecimalField(decimal_places=4, default=0.0, editable=False, max_digits=5)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('division', models.CharField(choices=[('TK', 'Tyke'), ('MN', 'Minor Novice'), ('NV', 'Novice'), ('MA', 'Minor Atom'), ('AT', 'Atom'), ('MP', 'Minor Peewee'), ('PW', 'Peewee'), ('MB', 'Minor Bantam'), ('BT', 'Bantam'), ('MM', 'Minor Midget'), ('MJ', 'Midget Junior'), ('MS', 'Midget Senior'), ('UD', 'Under 21')], default='MS', max_length=2)),
                ('season', models.CharField(choices=[('FN20', 'FINAL 2020'), ('SF20', 'SEMI-FINAL 2020'), ('PL20', 'Playoff 2020'), ('WY20', 'Winter Season 2020'), ('FY19', 'Fall Season 2019')], default='WY20', max_length=4)),
                ('level', models.CharField(choices=[('T1', 'Tier 1'), ('T2', 'Tier 2'), ('T3', 'Tier 3')], default='T1', max_length=2)),
                ('pl_group', models.CharField(blank=True, choices=[('G1', 'Group A'), ('G2', 'Group B')], default=None, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkwoods_app.topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
