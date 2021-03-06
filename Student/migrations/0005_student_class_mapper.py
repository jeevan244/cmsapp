# Generated by Django 4.0.6 on 2022-07-11 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_rename_course_id_class_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_class_mapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mapper', to='Student.student')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mapper', to='Student.class')),
            ],
        ),
    ]
