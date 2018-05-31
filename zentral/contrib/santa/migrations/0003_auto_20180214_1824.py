# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-14 18:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0037_auto_20180213_1407'),
        ('santa', '0002_collectedapplication_bundle_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('mode', models.IntegerField(choices=[(1, 'Monitor'), (2, 'Lockdown')], default=1)),
                ('file_changes_regex', models.TextField(blank=True, help_text='The regex of paths to log file changes. Regexes are specified in ICU format.')),
                ('whitelist_regex', models.TextField(blank=True, help_text="Matching binaries will be allowed to run, in both modes.Events will be logged with the 'ALLOW_SCOPE' decision.")),
                ('blacklist_regex', models.TextField(blank=True, help_text='In Monitor mode, executables whose paths are matched by this regex will be blocked.')),
                ('enable_page_zero_protection', models.BooleanField(default=True, help_text='If this flag is set to YES, 32-bit binaries that are missing the __PAGEZERO segment will be blocked even in MONITOR mode, unless the binary is whitelisted by an explicit rule.')),
                ('more_info_url', models.URLField(blank=True, help_text='The URL to open when the user clicks "More Info..." when opening Santa.app. If unset, the button will not be displayed.')),
                ('event_detail_url', models.URLField(blank=True, help_text='When the user gets a block notification, a button can be displayed which will take them to a web page with more information about that event.This property contains a kind of format string to be turned into the URL to send them to. The following sequences will be replaced in the final URL: %file_sha%, %machine_id%, %username%, %bundle_id%, %bundle_ver%.')),
                ('event_detail_text', models.TextField(blank=True, help_text='Related to the above property, this string represents the text to show on the button.')),
                ('unknown_block_message', models.TextField(default='The following application has been blocked from executing<br/>\nbecause its trustworthiness cannot be determined.', help_text='In Lockdown mode this is the message shown to the user when an unknown binary is blocked.')),
                ('banned_block_message', models.TextField(default='The following application has been blocked from executing<br/>\nbecause it has been deemed malicious.', help_text="This is the message shown to the user when a binary is blocked because of a rule if that rule doesn't provide a custom message.")),
                ('mode_notification_monitor', models.TextField(default='Switching into Monitor mode', help_text='The notification text to display when the client goes into Monitor mode.')),
                ('mode_notification_lockdown', models.TextField(default='Switching into Lockdown mode', help_text='The notification text to display when the client goes into Lockdown mode.')),
                ('machine_owner_plist', models.CharField(blank=True, help_text='The path to a plist that contains the machine owner key / value pair.', max_length=512)),
                ('machine_owner_key', models.CharField(blank=True, help_text='The key to use on the machine owner plist.', max_length=128)),
                ('batch_size', models.IntegerField(default=50, help_text='The number of rules to download or events to upload per request. Multiple requests will be made if there is more work than can fit in single request.', validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)])),
                ('bundles_enabled', models.BooleanField(default=False, help_text='if set, the bundle scanning feature is enabled.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.TextField(db_index=True)),
                ('machine_id', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='santa.Configuration')),
                ('secret', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.EnrollmentSecret')),
            ],
        ),
        migrations.AddField(
            model_name='enrolledmachine',
            name='enrollment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='santa.Enrollment'),
        ),
    ]