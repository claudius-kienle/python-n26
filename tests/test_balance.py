from n26.api import GET
from tests.test_api_base import N26TestBase, mock_requests


class BalanceTest(N26TestBase):
    """Balance tests"""

    @mock_requests(method=GET, response_file="balance.json")
    def test_balance_ok(self):
        result = self._underTest.get_balance()
        self.assertIsNotNone(result)
