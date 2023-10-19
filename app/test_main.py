import pytest
from unittest import mock
from app.main import can_access_google_page


@pytest.mark.parametrize(
    "valid_url, has_connection, can_access",
    [
        (True, True, "Accessible"),
        (False, True, "Not accessible"),
        (True, False, "Not accessible"),
        (False, False, "Not accessible"),
    ]
)
def test_can_access_google_page(valid_url: bool,
                                has_connection: bool,
                                can_access: str) -> None:
    with mock.patch("app.main.valid_google_url") as mock_url, \
         mock.patch("app.main.has_internet_connection") as mock_connection:
        mock_url.return_value = valid_url
        mock_connection.return_value = has_connection
        assert can_access_google_page("https://www.google.com") == can_access
