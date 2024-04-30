import datetime
from peewee import BooleanField, CharField, DateTimeField, Model


def create_migration_table(db):
    class BaseModel(Model):
        class Meta:
            database = db

    class MigrationStep(BaseModel):
        plugin_name = CharField()
        script_name = CharField()
        execution_date = DateTimeField(default=lambda: datetime.datetime.now())
        success = BooleanField()

        class Meta:
            indexes = (
                (('plugin_name', 'script_name'), True),
            )

    class MigrationController:
        def __init__(self):
            pass

        @staticmethod
        def setup_table_if_not_exists():
            db.create_tables([MigrationStep], safe=True)

        @staticmethod
        def get_step_status(plugin_name, step_name) -> MigrationStep:
            try:
                step = MigrationStep.get(MigrationStep.plugin_name == plugin_name,
                                         MigrationStep.script_name == step_name)
                return step
            except MigrationStep.DoesNotExist:
                return None

        @staticmethod
        def set_step_status(plugin_name, step_name, success):
            step = MigrationStep.get_or_none(
                plugin_name=plugin_name,
                script_name=step_name
            )
            if step is None:
                step = MigrationStep.create(
                    plugin_name=plugin_name,
                    script_name=step_name,
                    success=success,
                )
            else:
                step.success = success
                step.execution_date = datetime.datetime.now()
                step.save()

    return MigrationController
