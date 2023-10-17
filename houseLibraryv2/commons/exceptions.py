from rest_framework import status
from rest_framework.exceptions import APIException

# TODO - Atribuir a classe.
class HouseLibraryException(APIException):
    def __init__(self, error=None, data=None, status_code=status.HTTP_406_NOT_ACCEPTABLE, error_object=None,
                 origin='API HouseLibrary'):
        super().__init__(data)
        self.error = error
        self.data = data
        self.detail = {
            'status': 'ERROR',
            'origin': origin,
            'message': error_object if error_object else '{}: {}'.format(error, data)
        }
        self.status_code = status_code

    def __str__(self):
        import json
        return json.dumps(self.detail)

    def message(self):
        if self.data:
            return self.detail.get('message')
        else:
            return self.error


class IntegrityException(HouseLibraryException):

    def __init__(self, message: str):
        super().__init__(error=message, data=None, status_code=status.HTTP_400_BAD_REQUEST, error_object=None)