from os import environ
from pyairtable import Table


class AirTableApiController:

    # Init defined for pyairtable setup
    def __init__(
        self,
        api_key: str = environ.get("AIR_TABLE_API_KEY"),
        base_id: str = environ.get("AIR_TABLE_BASE_ID"),
        table_name: str = environ.get("AIR_TABLE_TABLE_NAME"),
    ) -> None:
        self.api_key = api_key
        self.base_id = base_id
        self.table_name = table_name
        self.table = Table(self.api_key, self.base_id, self.table_name)

    def get_record(self, id: str):
        return self.table.get(id)
