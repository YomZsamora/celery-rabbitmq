

class SerializerValidationsError(Exception):
    
    def __init__(self, message=None, detail=None) -> None:
        self.message = message
        self.detail = detail
        super().__init__(self.message, self.detail)
        
class DoesNotExist(Exception):
    
    status_code = 404
    
    def __init__(self, message=None) -> None:
        self.message = message
        super().__init__(self.message)
    