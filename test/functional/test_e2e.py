"""
"""
import pytest

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

class TestE2E():
    """
    The test will be on the request flow base on the perspective of every type of User, 
    this include the actions that are allowed for the user.
    """

    @pytest.mark.parametrize("user, password",[
        ("Ad_01","01Ad"),
        ("Em_01", "01Em"),
        ("Cl_01", "01Cl"),
        ("Cl_02", "Cl02")
    ])

    def test_request_flow(self, mocker, valid_acounts, user: str, password: str):

        mocker.patch("SystemFlow.logging", return_value = "Valid Acount")
        
        

