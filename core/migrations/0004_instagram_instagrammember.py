# Generated by Django 2.2 on 2019-04-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181024_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramMember',
            fields=[
                ('english_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('chinese_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=64)),
                ('collected_at', models.DateTimeField(auto_now_add=True)),
                ('is_buzzbird', models.BooleanField(default=False, verbose_name='Published to buzzbird Weibo?')),
                ('media_url', models.URLField()),
                ('link', models.URLField(db_index=True)),
                ('published_at', models.DateTimeField()),
                ('title', models.CharField(blank=True, max_length=1024)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='core.InstagramMember')),
            ],
        ),
    ]
