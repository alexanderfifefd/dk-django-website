from django.db import migrations, models


def migrate_lifecycle_values(apps, schema_editor):
    System = apps.get_model("pages", "System")
    System.objects.filter(stage="suggestion").update(stage="idea")

    Initiative = apps.get_model("pages", "Initiative")
    Initiative.objects.filter(status="proposal").update(status="proposed")
    Initiative.objects.filter(status="seeking-contributors").update(
        status="active",
        recruiting="open",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_initiative_dates"),
    ]

    operations = [
        migrations.AddField(
            model_name="system",
            name="recruiting",
            field=models.CharField(
                blank=True,
                choices=[("open", "Open")],
                default="",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="initiative",
            name="recruiting",
            field=models.CharField(
                blank=True,
                choices=[("open", "Open")],
                default="",
                max_length=20,
            ),
        ),
        migrations.RunPython(migrate_lifecycle_values, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="system",
            name="stage",
            field=models.CharField(
                choices=[
                    ("idea", "Idea"),
                    ("development", "Development"),
                    ("production", "Production"),
                ],
                default="production",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="initiative",
            name="status",
            field=models.CharField(
                choices=[
                    ("proposed", "Proposed"),
                    ("active", "Active"),
                    ("paused", "Paused"),
                    ("completed", "Completed"),
                ],
                default="active",
                max_length=30,
            ),
        ),
    ]
