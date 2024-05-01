#
# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
#
import time

from operator import attrgetter

import pytest

from _pytest.outcomes import fail

from snowflake.core import Clone, PointOfTimeOffset
from snowflake.core.database import Database, DatabaseCollection, DatabaseResource
from snowflake.core.exceptions import NotFoundError

from ..utils import random_string


pytestmark = pytest.mark.usefixtures("backup_database_schema", "use_rest")


@pytest.mark.skip_rest
@pytest.mark.jenkins
def test_fetch(databases, temp_db):
    database = databases[temp_db.name].fetch()
    assert (
        database.name.upper() == temp_db.name.upper()
    )
    assert database.comment == "created by temp_db"
    # Make sure that issuing an empty alter doesn't create a malformed SQL
    temp_db.create_or_update(database)


@pytest.mark.jenkins
def test_delete(databases):
    new_database = Database(
        name=random_string(5, "test_db_")
    )
    new_db = databases.create(new_database)
    new_db.delete()
    with pytest.raises(
        NotFoundError,
    ):
        new_db.fetch()


@pytest.mark.jenkins
def test_iter(databases, temp_db):
    assert any(
        map(
            lambda e: e
            in tuple(
                map(
                    attrgetter("name"),
                    databases.iter(),
                )
            ),
            (
                temp_db.name,  # for mixed case names
                temp_db.name.upper(),  # for upper/lower case names
            ),
        )
    )


@pytest.mark.jenkins
def test_iter_limit(databases):
    data = list(databases.iter(limit=10))
    assert len(data) <= 10


@pytest.fixture
def ensure_rest(session, root):
    root_orig_value = root._can_use_rest_api
    root._can_use_rest_api = True
    dbr_orig_value = DatabaseResource._supports_rest_api
    DatabaseResource._supports_rest_api = True
    try:
        session.sql("alter session set enable_snow_api_for_database='enable'").collect()
        yield
    finally:
        session.sql("alter session unset enable_snow_api_for_database").collect()
        root._can_use_rest_api = root_orig_value
        DatabaseResource._supports_rest_api = dbr_orig_value


# For the time being, create_or_update() over REST will not be supported for database.
# Verify the error message.
@pytest.mark.skip_bridge
@pytest.mark.jenkins
def test_create_or_update_database_unsupported(databases, temp_db: DatabaseResource, ensure_rest):
    try:
        db_def = temp_db.fetch()
        temp_db.create_or_update(db_def)
    except NotImplementedError as error:
        assert 'create_or_update is not yet supported' in str(error)
    else:
        fail('Expected exception was not raised.')


@pytest.mark.skip_rest
def test_create_or_update_database(databases, temp_db: DatabaseResource):
    db_def = temp_db.fetch()
    db_def.comment = "my new comment"
    db_def.data_retention_time_in_days = 0
    db_def.default_ddl_collation = "en_US-trim"
    db_def.log_level = "INFO"
    db_def.max_data_extension_time_in_days = 7
    db_def.suspend_task_after_num_failures = 1
    db_def.trace_level = "ALWAYS"
    db_def.user_task_managed_initial_warehouse_size = "SMALL"
    db_def.user_task_timeout_ms = 3600001
    temp_db.create_or_update(db_def)
    new_db = databases[temp_db.name].fetch()
    assert new_db.name in (temp_db.name, temp_db.name.upper())
    assert new_db.comment == "my new comment"
    assert new_db.data_retention_time_in_days == 0
    assert new_db.default_ddl_collation == "en_US-trim"
    assert new_db.log_level == "INFO"
    assert new_db.max_data_extension_time_in_days == 7
    assert new_db.suspend_task_after_num_failures == 1
    assert new_db.trace_level == "ALWAYS"
    assert new_db.user_task_managed_initial_warehouse_size == "SMALL"
    assert new_db.user_task_timeout_ms == 3600001


@pytest.mark.skip("Temporarily disabled. TODO: Investigate why this is flaky.")
@pytest.mark.jenkins
def test_create_clone(databases: DatabaseCollection):
    # for locally running this test run:
    #  create or replace database TESTDB_PYTHON DATA_RETENTION_TIME_IN_DAYS=1;
    time.sleep(1)
    new_db_def = Database(name=random_string(3, "test_database_create_clone_"))
    db = databases.create(
        new_db_def,
        clone=Clone(
            source="TESTDB_PYTHON_AUTO",
            point_of_time=PointOfTimeOffset(reference="before", when="-1")
        ),
        mode='orreplace',
    )
    try:
        # Try to reduce flakiness by sleeping
        time.sleep(10)
        db.fetch()
    finally:
        db.delete()


@pytest.mark.skip("Temporarily disabled. TODO: Investigate why this is flaky.")
@pytest.mark.env("online")
@pytest.mark.jenkins
def test_create_from_share(databases: DatabaseCollection):
    new_db_name = random_string(3, "test_db_from_share_")
    db = databases._create_from_share(
        new_db_name,
        share='SFSALESSHARED.SFC_SAMPLES_PROD3."SAMPLE_DATA"',
    )
    try:
        assert db.fetch().is_current
    finally:
        db.delete()


@pytest.mark.jenkins
def test_resist_multi_statement_sql_injection(databases: DatabaseCollection):
    new_db_name = random_string(3, "test_db_resist_multi_statement_sql_injection_")
    sql_injection_comment = "'comment for disguise'; select '1'"

    new_db = Database(
        name=new_db_name,
        comment=sql_injection_comment,
    )

    db = databases.create(new_db)
    try:
        db.fetch()
    finally:
        db.delete()


@pytest.mark.skip("This could only test in local dev-vm when set qa_mode = true")
@pytest.mark.jenkins
def test_fetch_with_long_running(
        databases,
        temp_db,
        setup_enable_rest_api_with_long_running,
        setup_with_connector_execution,
    ):
    alter_prefix = 'alter session '
    with setup_enable_rest_api_with_long_running(databases._ref_class),\
        setup_with_connector_execution(
            [
                alter_prefix + 'set TEST_SNOWAPI_TIME_OUT_REQUEST_ASYNC = true',
            ],
            [
                alter_prefix + 'unset TEST_SNOWAPI_TIME_OUT_REQUEST_ASYNC',
            ]
        ):

        database = databases[temp_db.name].fetch()
        assert (
            database.name.upper() == temp_db.name.upper()
        )


@pytest.mark.parametrize("comment", (None, "ThIs Is A cOmMeNt"))
@pytest.mark.skip_rest
@pytest.mark.jenkins
def test_update_comment(databases, comment):
    new_db_name = random_string(3, "test_update_comment_")
    new_db = Database(name=new_db_name)
    d = databases.create(new_db)
    try:
        new_db.comment = comment
        d.create_or_update(new_db)
        assert d.fetch().comment == comment
    finally:
        d.delete()
