from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:


    def __init__(self, path_id: int,start_location: Habitat,  current_location: str,
                    destination: Habitat, duration: Optional[int] = None)  -> None:
        
        self.path_id = path_id
        self.start_location = start_location
        self.current_location = current_location
        self.destination = destination
        self.duration = duration
    
    def get_migration_path_details(self,path_id) -> dict:
            pass
    
    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
            pass
    