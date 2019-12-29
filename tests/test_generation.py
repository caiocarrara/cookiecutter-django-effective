import pytest

@pytest.fixture
def context():
    return {
        "project_name": "My Test Project",
        "project_slug": "my_test_project",
        "description": "This is a test project",
        "author_name": "Tester Blaster",
        "company_name": "The Test LLC",
    }


def test_project_generation(cookies, context):
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]