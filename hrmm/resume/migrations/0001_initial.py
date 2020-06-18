# Generated by Django 3.0.5 on 2020-05-31 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('height', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(max_length=255)),
                ('birthday', models.CharField(max_length=255)),
                ('hukou_address', models.CharField(blank=True, max_length=255, null=True)),
                ('hukou_address_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('hometown_address', models.CharField(blank=True, max_length=255, null=True)),
                ('hometown_address_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('id_card', models.CharField(blank=True, max_length=255, null=True)),
                ('race', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('polit_status', models.CharField(blank=True, max_length=255, null=True)),
                ('languages', models.CharField(blank=True, max_length=255, null=True)),
                ('english_level', models.CharField(blank=True, max_length=255, null=True)),
                ('computer_level', models.CharField(blank=True, max_length=255, null=True)),
                ('blog', models.CharField(blank=True, max_length=255, null=True)),
                ('work_year', models.CharField(blank=True, max_length=255, null=True)),
                ('work_year_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('work_year_inf', models.CharField(blank=True, max_length=255, null=True)),
                ('work_start_time', models.DateField(blank=True, null=True)),
                ('work_position', models.CharField(blank=True, max_length=255, null=True)),
                ('work_company', models.CharField(blank=True, max_length=255, null=True)),
                ('work_industry', models.CharField(blank=True, max_length=255, null=True)),
                ('work_status', models.CharField(blank=True, max_length=255, null=True)),
                ('work_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('work_salary_min', models.IntegerField(blank=True, null=True)),
                ('work_salary_max', models.IntegerField(blank=True, null=True)),
                ('work_location', models.CharField(blank=True, max_length=255, null=True)),
                ('work_location_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('work_job_nature', models.CharField(blank=True, max_length=255, null=True)),
                ('has_oversea_edu', models.BooleanField(default=False)),
                ('has_oversea_exp', models.BooleanField(default=False)),
                ('grad_time', models.DateField()),
                ('college', models.CharField(max_length=255)),
                ('college_type', models.CharField(blank=True, max_length=255, null=True)),
                ('college_rank', models.CharField(blank=True, max_length=255, null=True)),
                ('college_dept', models.CharField(blank=True, max_length=255, null=True)),
                ('major', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('recruit', models.CharField(blank=True, max_length=255, null=True)),
                ('resume_type', models.CharField(blank=True, max_length=250, null=True)),
                ('resume_source', models.CharField(blank=True, max_length=250, null=True)),
                ('resume_id', models.CharField(blank=True, max_length=250, null=True)),
                ('resume_name', models.CharField(blank=True, max_length=250, null=True)),
                ('resume_parse_time', models.DateTimeField(auto_now_add=True)),
                ('resume_update_time', models.DateTimeField(blank=True, null=True)),
                ('resume_integrity', models.IntegerField(blank=True, null=True)),
                ('expect_job', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_cpy', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_salary', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_salary_min', models.IntegerField(blank=True, null=True)),
                ('expect_salary_max', models.IntegerField(blank=True, null=True)),
                ('expect_industry', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_duty_time', models.DateField(blank=True, null=True)),
                ('expect_jnature', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_jstatus', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_jlocation', models.CharField(blank=True, max_length=250, null=True)),
                ('expect_jlocation_norm', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('org', models.CharField(blank=True, max_length=255, null=True)),
                ('loc', models.CharField(blank=True, max_length=255, null=True)),
                ('cert', models.CharField(max_length=255)),
                ('cont', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('train_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('cpy', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('resp', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(blank=True, max_length=255, null=True)),
                ('language_level', models.CharField(blank=True, max_length=255, null=True)),
                ('language_read_write', models.CharField(blank=True, max_length=255, null=True)),
                ('language_listen_speak', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languagedetails', to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Jobexp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('cpy', models.CharField(blank=True, max_length=255, null=True)),
                ('cpy_nature', models.CharField(blank=True, max_length=255, null=True)),
                ('cpy_size', models.CharField(blank=True, max_length=255, null=True)),
                ('cpy_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('dept', models.CharField(blank=True, max_length=255, null=True)),
                ('nature', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('staff', models.CharField(blank=True, max_length=255, null=True)),
                ('report_to', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('why_leave', models.CharField(blank=True, max_length=255, null=True)),
                ('duaraton', models.CharField(blank=True, max_length=255, null=True)),
                ('capacity', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.CharField(blank=True, max_length=1024, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('college', models.CharField(blank=True, max_length=255, null=True)),
                ('college_type', models.CharField(blank=True, max_length=255, null=True)),
                ('college_rank', models.CharField(blank=True, max_length=255, null=True)),
                ('college_dept', models.CharField(blank=True, max_length=255, null=True)),
                ('major', models.CharField(blank=True, max_length=255, null=True)),
                ('recruit', models.CharField(blank=True, max_length=255, null=True)),
                ('gpa', models.CharField(blank=True, max_length=255, null=True)),
                ('degree', models.CharField(blank=True, max_length=255, null=True)),
                ('degree_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='resume.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('qq', models.CharField(blank=True, max_length=255, null=True)),
                ('weixin', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('city_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('living_address', models.CharField(blank=True, max_length=255, null=True)),
                ('living_address_norm', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contactdetail', to='resume.Resume')),
            ],
        ),
    ]
