from operator import attrgetter

import pytest

from snowflake.core import Clone, PointOfTimeOffset
from snowflake.core.exceptions import NotFoundError
from snowflake.core.schema import Schema, SchemaCollection, SchemaResource

from .utils import random_string


pytestmark = pytest.mark.usefixtures("backup_database_schema", "use_rest")


@pytest.mark.skip_rest
@pytest.mark.jenkins
def test_fetch(temp_schema):
    schema = temp_schema.fetch()
    assert (
        schema.name == temp_schema.name  # for mixed case names
        or temp_schema.name.upper()
        == temp_schema.name.upper()  # for upper/lower case names
    )
    # Make sure that issuing an empty alter doesn't create a malformed SQL
    temp_schema.create_or_update(schema)


@pytest.mark.jenkins
def test_delete(schemas):
    comment = "my comment"
    new_schema = Schema(
        name=random_string(5, "test_schema_"),
        comment=comment,
    )
    s = schemas.create(new_schema)
    assert s.fetch().comment == comment
    s.delete()
    with pytest.raises(
        NotFoundError,
    ):
        s.fetch()


def test_iter(schemas, temp_schema):
    schema_names = tuple(
                map(
                    attrgetter("name"),
                    schemas.iter(),
                )
    )
    assert any(
        map(
            lambda e: e
            in schema_names,
            (
                temp_schema.name,  # for mixed case names
                temp_schema.name.upper(),  # for upper/lower case names
            ),
        )
    )


@pytest.mark.jenkins
def test_iter_limit(schemas):
    data = list(schemas.iter(limit=10))
    assert len(data) <= 10


@pytest.mark.skip_rest
def test_update_all_params(schemas, temp_schema: SchemaResource):
    new_sc_def = temp_schema.fetch()
    new_sc_def.comment = "my new comment"
    new_sc_def.data_retention_time_in_days = 0
    new_sc_def.default_ddl_collation = "en_US-trim"
    new_sc_def.log_level = "INFO"
    new_sc_def.pipe_execution_paused = True
    new_sc_def.max_data_extension_time_in_days = 7
    new_sc_def.suspend_task_after_num_failures = 1
    new_sc_def.trace_level = "ALWAYS"
    new_sc_def.user_task_managed_initial_warehouse_size = "SMALL"
    new_sc_def.user_task_timeout_ms = 3600001
    temp_schema.create_or_update(new_sc_def)
    new_sc = schemas[temp_schema.name].fetch()
    assert new_sc.name in (temp_schema.name, temp_schema.name.upper())
    assert new_sc.comment == "my new comment"
    assert new_sc.data_retention_time_in_days == 0
    assert new_sc.default_ddl_collation == "en_US-trim"
    assert new_sc.log_level == "INFO"
    assert new_sc.pipe_execution_paused is True
    assert new_sc.max_data_extension_time_in_days == 7
    assert new_sc.suspend_task_after_num_failures == 1
    assert new_sc.trace_level == "ALWAYS"
    assert new_sc.user_task_managed_initial_warehouse_size == "SMALL"
    assert new_sc.user_task_timeout_ms == 3600001


@pytest.mark.jenkins
@pytest.mark.skip("Temporarily disabled. TODO: Investigate why this is flaky.")
def test_create_clone(schemas: SchemaCollection, temp_schema: SchemaResource):
    # for locally running this test run:
    #  create or replace schema TESTDB_PYTHON DATA_RETENTION_TIME_IN_DAYS=1;
    new_schema_def = Schema(name="TEST_CLONE_TESTSCHEMA_PYTHON")
    schema = schemas.create(
        new_schema_def,
        clone=Clone(
            source="PUBLIC",
            point_of_time=PointOfTimeOffset(reference="at", when="-5")
        ),
        mode='orreplace',
    )
    try:
        schema.fetch()
    finally:
        schema.delete()


@pytest.mark.parametrize("comment", (None, "ThIs Is A cOmMeNt"))
@pytest.mark.jenkins
@pytest.mark.skip_rest
def test_update_comment(schemas, comment):
    new_s_name = random_string(3, "test_update_comment_")
    new_s = Schema(name=new_s_name)
    s = schemas.create(new_s)
    try:
        new_s.comment = comment
        s.create_or_update(new_s)
        assert s.fetch().comment == comment
    finally:
        s.delete()
