# Generated by Django 4.0.6 on 2022-07-14 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
        ('Student', '0006_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classcourse', to='Student.course'),
        ),
        migrations.AlterField(
            model_name='class',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classsession', to='Student.session'),
        ),
        migrations.AlterField(
            model_name='student_class_mapper',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mapperclass', to='Student.class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectclass', to='Student.class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjectteacher', to='Teacher.teacher'),
        ),
    ]
