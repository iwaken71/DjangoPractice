# Generated by Django 3.2.6 on 2021-08-05 06:20

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
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('code', models.TextField(blank=True, verbose_name='コード')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
    ]
