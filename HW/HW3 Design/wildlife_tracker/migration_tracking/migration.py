from typing import Any

class Migration:


    def __init__(self, migration_id: int, status: str = "Scheduled")  -> None:
        self.migration_id = migration_id
        self.status = status
         

    def update_migration_details(self,migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migration_details(self,migration_id: int) -> dict[str, Any]:
        pass