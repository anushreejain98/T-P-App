# Generated by Django 2.1.3 on 2018-12-05 10:05

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_name', models.CharField(help_text='This is the grey text', max_length=30)),
                ('branch_appl', models.CharField(choices=[('CS', 'CS'), ('EE', 'EE'), ('ME', 'ME'), ('CB', 'CB'), ('CE', 'CE')], max_length=30)),
                ('cpi_req', models.DecimalField(decimal_places=2, default='0', max_digits=4)),
                ('course_appl', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('M.Sc', 'M.Sc')], max_length=30)),
                ('stipend', models.IntegerField(null=True)),
                ('ctc', models.IntegerField(null=True)),
                ('test_date', models.DateField(null=True)),
                ('job_desc', models.CharField(max_length=800, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1')], default='B1', max_length=2)),
                ('hr_name', models.CharField(default='-', max_length=30)),
                ('hr_contact', models.EmailField(max_length=100, unique=True)),
                ('sector', models.CharField(default='IT', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30)),
                ('cpi', models.DecimalField(decimal_places=2, default='0', max_digits=4)),
                ('dept', models.CharField(choices=[('CS', 'CS'), ('EE', 'EE'), ('ME', 'ME'), ('CB', 'CB'), ('CE', 'CE')], default='-', max_length=30)),
                ('course', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('M.Sc', 'M.Sc')], default='-', max_length=30)),
                ('resume', models.URLField()),
                ('webmail', models.EmailField(max_length=100, unique=True)),
                ('avatar', models.ImageField(default='images/default.png', upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='pos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpcm_app.JobPosition'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='cmp_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpcm_app.Company'),
        ),
        migrations.AddField(
            model_name='application',
            name='stud',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tpcm_app.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='jobposition',
            unique_together={('cmp_name', 'pos_name')},
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together={('pos', 'stud')},
        ),
    ]
