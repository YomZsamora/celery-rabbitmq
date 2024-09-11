from rest_framework import status

ERROR_STATUS = "error"
SUCCESS_STATUS = "success"

class ApiResponse:
    
    def __init__(self):
        self.code = status.HTTP_200_OK
        self.status = SUCCESS_STATUS
        self.message = ""
        self.data: list[any] | None
        