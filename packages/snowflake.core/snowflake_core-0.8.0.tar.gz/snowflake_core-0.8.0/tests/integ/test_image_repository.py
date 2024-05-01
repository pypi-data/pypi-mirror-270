#
# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
#

from operator import attrgetter

import pytest

from snowflake.core.exceptions import NotFoundError
from snowflake.core.image_repository import ImageRepository

from ..utils import random_string


pytestmark = pytest.mark.usefixtures("use_rest")


def test_fetch(image_repositories, temp_ir):
    ir: ImageRepository = image_repositories[temp_ir.name].fetch()
    assert (
        ir.name == temp_ir.name  # for mixed case names
        or ir.name.upper() == temp_ir.name.upper()  # for upper/lower case names
    )
    assert ir.created_on
    assert ir.repository_url


def test_delete(image_repositories):
    ir_name = random_string(5, "test_ir_")
    test_ir = ImageRepository(
        name=ir_name,
    )
    image_repositories.create(test_ir)
    image_repositories[test_ir.name].delete()
    with pytest.raises(
        NotFoundError,
    ):
        image_repositories[test_ir.name].fetch()


def test_iter(image_repositories, temp_ir):
    assert any(
        map(
            lambda e: e
            in tuple(
                map(
                    attrgetter("name"),
                    image_repositories.iter(),
                )
            ),
            (
                temp_ir.name,  # for mixed case names
                temp_ir.name.upper(),  # for upper/lower case names
            ),
        )
    )


@pytest.mark.skip(reason="put isn't supported be Image repository OAS")
@pytest.mark.parametrize("comment", (None, "ThIs Is A cOmMeNt"))
def test_update_comment(image_repositories, comment):
    new_ir_name = random_string(3, "test_update_comment_")
    new_ir = ImageRepository(name=new_ir_name)
    ir = image_repositories.create(new_ir)
    try:
        new_ir.comment = comment
        ir.create_or_update(new_ir)
        assert ir.fetch().comment == comment
    finally:
        ir.delete()
