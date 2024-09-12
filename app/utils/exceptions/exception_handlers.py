from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError

from utils.views.responses import ApiResponse, ERROR_STATUS
from utils.exceptions.custom_exceptions import SerializerValidationsError

def custom_exception_handler(exc, context):
    
    api_response = ApiResponse()
    api_response.status = ERROR_STATUS
    
    if isinstance(exc, SerializerValidationsError):
        api_response.code = ValidationError.status_code
        api_response.message = exc.message
        if exc.detail is not None:
            api_response.data = exc.detail
        return Response(vars(api_response), api_response.code)
    
    return exception_handler(exc, context)
    