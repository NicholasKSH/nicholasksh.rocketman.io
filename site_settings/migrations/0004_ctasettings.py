# Generated by Django 3.2.9 on 2021-12-01 07:50

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('site_settings', '0003_hourssettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CtaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('internal_page', models.ForeignKey(blank=True, help_text='Select a internal Wagtail page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
