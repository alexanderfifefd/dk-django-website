from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="system",
            name="stage",
            field=models.CharField(
                choices=[
                    ("suggestion", "Suggestion"),
                    ("development", "Development"),
                    ("production", "Production"),
                ],
                default="production",
                max_length=20,
            ),
        ),
    ]
