# Generated by Django 3.0.7 on 2020-06-24 19:26

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('flance', '0002_auto_20200624_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company', models.CharField(max_length=100)),
                ('company_website', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name': 'Employer',
                'verbose_name_plural': 'Employers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='freelancer',
            name='github',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='salary',
            field=models.IntegerField(default=250, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(250)]),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='fields',
            field=models.CharField(choices=[('DESKTOP_APP', 'Desktop App Developer'), ('ANDROID_APP', 'Android App Developer'), ('IOS_APP', 'iOS App Developer'), ('WEB_APP', 'Web App Developer'), ('ML', 'Machine Learning'), ('AI', 'Artificial Intelligence')], max_length=50),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='languages',
            field=models.CharField(choices=[('VISUAL_BASIC_NET', 'Visual Basic .NET'), ('OBJECTIVE_C', 'Objective-C'), ('JAVASCRIPT', 'JavaScript'), ('PYTHON', 'Python'), ('C_HASH', 'C#'), ('SWIFT', 'Swift'), ('JAVA', 'Java'), ('RUBY', 'Ruby'), ('PERL', 'Perl'), ('CPP', 'C++'), ('PHP', 'PHP'), ('SQL', 'SQL'), ('GO', 'Go'), ('C', 'C'), ('R', 'R')], max_length=50),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='level',
            field=models.CharField(choices=[('BEG', 'Beginner'), ('EXP', 'Experienced'), ('PRO', 'Pro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='specialization',
            field=models.CharField(choices=[('FED', 'Front End Developer'), ('BED', 'Back End Developer'), ('FSD', 'Full Stack Developer')], max_length=50),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_for_completion', models.IntegerField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flance.Employer')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(choices=[('VISUAL_BASIC_NET', 'Visual Basic .NET'), ('OBJECTIVE_C', 'Objective-C'), ('JAVASCRIPT', 'JavaScript'), ('PYTHON', 'Python'), ('C_HASH', 'C#'), ('SWIFT', 'Swift'), ('JAVA', 'Java'), ('RUBY', 'Ruby'), ('PERL', 'Perl'), ('CPP', 'C++'), ('PHP', 'PHP'), ('SQL', 'SQL'), ('GO', 'Go'), ('C', 'C'), ('R', 'R')], max_length=50)),
                ('fields', models.CharField(choices=[('DESKTOP_APP', 'Desktop App Developer'), ('ANDROID_APP', 'Android App Developer'), ('IOS_APP', 'iOS App Developer'), ('WEB_APP', 'Web App Developer'), ('ML', 'Machine Learning'), ('AI', 'Artificial Intelligence')], max_length=50)),
                ('specialization', models.CharField(choices=[('FED', 'Front End Developer'), ('BED', 'Back End Developer'), ('FSD', 'Full Stack Developer')], max_length=50)),
                ('level', models.CharField(choices=[('BEG', 'Beginner'), ('EXP', 'Experienced'), ('PRO', 'Pro')], max_length=20)),
                ('salary', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(250)])),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flance.Job')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
