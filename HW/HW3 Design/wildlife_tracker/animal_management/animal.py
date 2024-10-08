from typing import Any, Optional

class Animal:
    def __init__(self, 
                 animal_id: int) -> None:
        
    
        age: Optional[int] = None
    

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass