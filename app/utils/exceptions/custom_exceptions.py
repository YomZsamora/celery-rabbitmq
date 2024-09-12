

class SerializerValidationsError(Exception):
    
    def __init__(self, message=None, detail=None) -> None:
        self.message = message
        self.detail = detail
        super().__init__(self.message, self.detail)
        
    