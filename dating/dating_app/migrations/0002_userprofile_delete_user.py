# Generated by Django 5.0.1 on 2024-01-08 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='Gender')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('bundesland', models.CharField(blank=True, choices=[('BW', 'Baden-Württemberg'), ('BY', 'Bavaria (Bayern)'), ('BE', 'Berlin'), ('BL', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hesse'), ('MV', 'Mecklenburg-Western Pomerania (Mecklenburg-Vorpommern)'), ('NI', 'Lower Saxony (Niedersachsen)'), ('NW', 'North Rhine-Westphalia (Nordrhein-Westfalen)'), ('RP', 'Rhineland-Palatinate (Rheinland-Pfalz)'), ('SL', 'Saarland'), ('SA', 'Saxony (Sachsen)'), ('SN', 'Saxony-Anhalt'), ('ST', 'Schleswig-Holstein'), ('TH', 'Thuringia (Thüringen)')], max_length=2, null=True, verbose_name='Bundesland')),
                ('language', models.CharField(blank=True, max_length=100, null=True, verbose_name='Language')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Height (in cm)')),
                ('weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weight (in kg)')),
                ('eye_color', models.CharField(blank=True, choices=[('brown', 'Brown'), ('black', 'Black'), ('blue', 'Blue'), ('green', 'Green'), ('gray', 'Gray'), ('hazel', 'Hazel')], max_length=10, null=True, verbose_name='Eye Color')),
                ('hair_color', models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('blond', 'Blond'), ('red', 'Red'), ('gray', 'Gray')], max_length=10, null=True, verbose_name='Hair Color')),
                ('education', models.CharField(blank=True, choices=[('high_school', 'High School'), ('college', 'College'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('phd', 'Ph.D.'), ('other', 'Other')], max_length=11, null=True, verbose_name='Education')),
                ('occupation', models.CharField(blank=True, choices=[('employed', 'Employed'), ('unemployed', 'Unemployed'), ('student', 'Student'), ('freelancer', 'Freelancer'), ('retired', 'Retired'), ('other', 'Other')], max_length=10, null=True, verbose_name='Occupation')),
                ('hobbies', models.TextField(blank=True, null=True, verbose_name='Hobbies')),
                ('interests', models.TextField(blank=True, null=True, verbose_name='Interests')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('relationship_purpose', models.CharField(blank=True, choices=[('flirt', 'Flirt'), ('marriage', 'Marriage'), ('pen_friends', 'Pen Friends'), ('spend_time_together', 'Spend Time Together')], max_length=20, null=True, verbose_name='Relationship Purpose')),
                ('looking_for', models.CharField(blank=True, choices=[('man', 'Man'), ('woman', 'Woman'), ('diverse', 'Diverse')], max_length=10, null=True, verbose_name='Looking For')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
