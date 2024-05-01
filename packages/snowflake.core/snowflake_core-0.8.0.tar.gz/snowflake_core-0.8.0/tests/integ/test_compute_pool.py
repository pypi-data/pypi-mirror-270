#
# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
#
from contextlib import suppress
from textwrap import dedent

import pytest

from snowflake.core.compute_pool import ComputePool, ComputePoolResource
from snowflake.core.exceptions import APIError, NotFoundError
from snowflake.core.service import Service, ServiceSpecInlineText

from ..utils import random_string


pytestmark=pytest.mark.usefixtures("use_rest")


def test_fetch(compute_pools, temp_cp):
    cp_ref = compute_pools[temp_cp.name]
    cp = cp_ref.fetch()
    assert (
        cp.name == temp_cp.name  # for mixed case names
        or cp.name.upper() == temp_cp.name.upper()  # for upper/lower case names
    )
    assert cp.min_nodes == 1
    assert cp.max_nodes == 1
    assert cp.created_on
    assert cp.comment == "created by temp_cp"
    # Make sure that issuing an empty alter doesn't create a malformed SQL
    cp_ref.create_or_update(cp)

def test_delete(compute_pools):
    cp_name = random_string(5, "test_cp_")
    test_cp = ComputePool(
        name=cp_name,
        instance_family="STANDARD_1",
        min_nodes=1,
        max_nodes=1,
    )
    compute_pools.create(test_cp)
    compute_pools[test_cp.name].delete()
    with pytest.raises(
        NotFoundError,
    ):
        compute_pools[test_cp.name].fetch()


def test_iter(compute_pools, temp_cp):
    for cp in compute_pools.iter(like=temp_cp.name):
        assert cp.name in (
            temp_cp.name,  # for mixed case names
            temp_cp.name.upper(),  # for upper/lower case names
        )
        assert cp.instance_family == "STANDARD_1"
        assert cp.min_nodes == 1
        assert cp.max_nodes == 1


def test_suspend_resume(compute_pools, temp_cp):
    assert compute_pools[temp_cp.name].fetch().state in (
        "IDLE",
        "RUNNING",
        "STARTING",
    )
    compute_pools[temp_cp.name].suspend()
    assert compute_pools[temp_cp.name].fetch().state == "SUSPENDED"
    compute_pools[temp_cp.name].resume()
    assert compute_pools[temp_cp.name].fetch().state in (
        "IDLE",
        "RUNNING",
        "STARTING",
        "IDLE",
    )


def test_stop_all_services(compute_pools, services, imagerepo, temp_cp):
    s_name = random_string(5, "test_service_")
    inline_spec = dedent(
        f"""
            spec:
              containers:
              - name: hello-world
                image: {imagerepo}/hello-world:latest
             """
    )
    test_s = Service(
        name=s_name,
        compute_pool=temp_cp.name,
        spec=ServiceSpecInlineText(spec_text=inline_spec),
        min_instances=1,
        max_instances=1,
    )
    services.create(test_s)

    services_in_pool = [service for service in services.iter() if service.compute_pool == temp_cp.name.upper()]
    assert len(services_in_pool) == 1
    assert services_in_pool[0].name == test_s.name.upper()
    compute_pools[temp_cp.name].stop_all_services()
    services_in_pool = [service for service in services.iter() if service.compute_pool == temp_cp.name.upper()]
    assert len(services_in_pool) == 0


def test_create_or_update_compute_pool(compute_pools, root):
    if root._can_use_rest_api and ComputePoolResource._supports_rest_api:
        pytest.skip("createOrAlterComputePool not currently supported by SnowAPI")

    cp_name = random_string(5, "test_cp_")
    comment = "CoMpLiCaTeD sTrInG"
    test_cp = ComputePool(
        name=cp_name,
        instance_family="STANDARD_1",
        min_nodes=1,
        max_nodes=1,
        auto_resume=False,
        comment=comment,
    )
    cp_ref = compute_pools[cp_name]
    cp_ref.create_or_update(test_cp)
    try:
        fetched = cp_ref.fetch()
        assert fetched.instance_family == "STANDARD_1"
        assert fetched.min_nodes == 1
        assert fetched.max_nodes == 1
        assert fetched.auto_resume is False
        assert fetched.comment == comment

        fetched.min_nodes = 2
        fetched.max_nodes = 2
        fetched.auto_resume = None
        cp_ref.create_or_update(fetched)
        fetched_again = cp_ref.fetch()
        assert fetched_again.instance_family == "STANDARD_1"
        assert fetched_again.min_nodes == 2
        assert fetched_again.max_nodes == 2
        assert fetched_again.auto_resume is True
        assert fetched_again.comment == comment

        with pytest.raises(APIError) as exinfo:
            fetched.instance_family = "STANDARD_2"
            cp_ref.create_or_update(fetched)
        assert exinfo.match("instance_family` of a computer pool can't be changed")
        assert exinfo.value.status == 400
    finally:
        with suppress(NotFoundError):
            cp_ref.delete()


@pytest.mark.parametrize("comment", (None, "ThIs Is A cOmMeNt"))
def test_update_comment(compute_pools, comment, request):
    if "rest" in request.node.callspec.id:
        pytest.xfail("Rest doesn't support updating a compute pool")
    new_cp_name = random_string(3, "test_update_comment_")
    new_cp = ComputePool(
        name=new_cp_name,
        min_nodes=1,
        max_nodes=1,
        instance_family="CPU_X64_XS",
    )
    cp = compute_pools.create(new_cp)
    try:
        new_cp.comment = comment
        cp.create_or_update(new_cp)
        assert cp.fetch().comment == comment
    finally:
        cp.delete()
