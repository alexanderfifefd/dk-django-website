from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_system_stage"),
    ]

    operations = [
        migrations.AddField(
            model_name="system",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]
