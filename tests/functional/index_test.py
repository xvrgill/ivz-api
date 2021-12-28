class TestIndex:
    def test_status_code_200(self, client) -> None:
        r = client.get("/index")
        assert r.status_code == 200

    def test_index_json_response(self, client) -> None:
        r = client.get("/index")
        assert "Hello World" in r.json
