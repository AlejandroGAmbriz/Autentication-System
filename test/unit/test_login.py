"""
"""
import pytest
from classes.system_flow import SystemFlow

@pytest.fixture
def valid_acounts():
    """
    Mock for our Acount DB
    """
    return [
            {"acount": "Ad_01", "password": "01Ad"},
            {"acount": "Em_01", "password": "01Em"},
            {"acount": "Cl_01", "password": "01Cl"},
            {"acount": "Cl_02", "password": "Cl02"}
        ]
class TestLog():
    """Test for loging feature
    """
    @pytest.mark.parametrize("user, password",[
        ("Ad_01","01Ad"),
        ("Em_01", "01Em"),
        ("Cl_01", "01Cl"),
        ("Cl_02", "Cl02")
    ])

    def test_log_succes(self, valid_acounts , user: str, password: str):

        flow = SystemFlow(valid_acounts)
        result = flow.log_verification(user, password)

        assert result is True

    def test_log_fail(self, valid_acounts):
        user = "Fail_01"
        password = "01FA"
        flow = SystemFlow(valid_acounts)
        result = flow.log_verification(user, password)

        assert result is False
