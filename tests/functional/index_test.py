import pytest


class TestIndex:
    def test_status_code_200(self, client) -> None:
        r = client.get("/index")
        assert r.status_code == 200
        print

    def test_status_code_404(self, client) -> None:
        with pytest.raises(AssertionError, match="404"):
            r = client.get("/random_endpoint")
            assert r.status_code == 200

    def test_index_json_response(self, client) -> None:
        r = client.get("/index")
        assert "Hello World" in r.json
