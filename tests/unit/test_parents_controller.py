from unittest.mock import patch
from app.schemas.Schema import ParentSchema


def test_parent_data_model_dump():
    parent_data = ParentSchema(
        first_name="Mondddd",
        last_name="Doe",
        address_street="123 Main St",
        address_city="Anytown",
        address_state="CA",
        address_zip="12345"
    )

    expected_dict = {
        "first_name": "Mondddd",
        "last_name": "Doe",
        "address_street": "123 Main St",
        "address_city": "Anytown",
        "address_state": "CA",
        "address_zip": "12345",
        "children": []
    }

    with patch("app.controllers.parent_controller.create") as mock_create:
        parent_dict = parent_data.model_dump()
        assert parent_dict == expected_dict
        mock_create.assert_not_called()
