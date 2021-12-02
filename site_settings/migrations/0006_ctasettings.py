# Generated by Django 3.2.9 on 2021-12-01 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('site_settings', '0005_delete_ctasettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CtaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField(blank=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('link_title', models.TextField(blank=True)),
                ('link_page', models.ForeignKey(blank=True, help_text='Select a internal Wagtail page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
