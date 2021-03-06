# Generated by Django 2.1.5 on 2019-03-06 12:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='act',
            fields=[
                ('actId', models.IntegerField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('caption', models.CharField(max_length=200)),
                ('upvotes', models.IntegerField(default=0)),
                ('imgB64', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('categoryName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('categoryCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=400, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=42)),
            ],
        ),
        migrations.AddField(
            model_name='act',
            name='categoryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
        migrations.AddField(
            model_name='act',
            name='username',
            field=models.ForeignKey(default='johndoe==', on_delete=django.db.models.deletion.SET_DEFAULT, to='app.user'),
        ),
    ]
