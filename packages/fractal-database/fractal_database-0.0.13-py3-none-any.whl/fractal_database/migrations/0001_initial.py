import django.core.serializers.json
import django.db.models.deletion
import fractal_database.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppCatalog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('app_ids', models.JSONField(default=list)),
                ('git_url', models.URLField()),
                ('checksum', models.CharField(max_length=255)),
                ('public', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_root', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('owner_matrix_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('url', models.URLField()),
                ('sync_token', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DatabaseConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('singleton', fractal_database.fields.SingletonField(default=True, unique=True)),
                ('current_db', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fractal_database.database')),
                ('current_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fractal_database.device')),
            ],
        ),
        migrations.AddField(
            model_name='database',
            name='devices',
            field=models.ManyToManyField(to='fractal_database.device'),
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('app_instance_id', models.CharField(max_length=255, unique=True)),
                ('metadata', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fractal_database.appcatalog')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to='fractal_database.database')),
                ('devices', models.ManyToManyField(to='fractal_database.device')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReplicatedInstanceConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('object_id', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_content_type', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DummyReplicationTarget',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('enabled', models.BooleanField(default=True)),
                ('filter', models.CharField(blank=True, max_length=255, null=True)),
                ('primary', models.BooleanField(default=False)),
                ('metadata', models.JSONField(default=dict)),
                ('database', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fractal_database.database')),
                ('instances', models.ManyToManyField(to='fractal_database.replicatedinstanceconfig')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepresentationLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('target_id', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=255)),
                ('object_id', models.CharField(max_length=255)),
                ('metadata', models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_content_type', to='contenttypes.contenttype')),
                ('target_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_target_type', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReplicationLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('payload', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('object_version', models.PositiveIntegerField(default=0)),
                ('target_id', models.CharField(max_length=255)),
                ('object_id', models.CharField(max_length=255)),
                ('instance_version', models.PositiveIntegerField(default=0)),
                ('txn_id', models.CharField(blank=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_content_type', to='contenttypes.contenttype')),
                ('target_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_target_type', to='contenttypes.contenttype')),
                ('repr_logs', models.ManyToManyField(to='fractal_database.representationlog')),
            ],
        ),
        migrations.AddConstraint(
            model_name='databaseconfig',
            constraint=models.UniqueConstraint(condition=models.Q(('singleton', True)), fields=('singleton',), name='unique_database_singleton'),
        ),
        migrations.AddConstraint(
            model_name='dummyreplicationtarget',
            constraint=models.UniqueConstraint(condition=models.Q(('primary', True)), fields=('database',), name='fractal_database_dummyreplicationtarget_unique_primary_per_database'),
        ),
        migrations.AddIndex(
            model_name='replicationlog',
            index=models.Index(fields=['content_type', 'object_id'], name='fractal_dat_content_59a6e8_idx'),
        ),
    ]
