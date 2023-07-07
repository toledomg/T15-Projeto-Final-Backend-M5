from rest_framework.views import Request, Response, status

class ResponseMethods:
    def response_success(status_code, params="Deleted method"):
        match status_code:
            case 200:
                status_code = status.HTTP_200_OK
            case 201:
                status_code = status.HTTP_201_CREATED
            case 204:
                status_code = status.HTTP_204_NO_CONTENT
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(params, status_code)

    def response_error(status_code, params="Error method"):
        match status_code:
            case 400:
                status_code = status.HTTP_400_BAD_REQUEST
        return Response(params, status_code)

    def block_user_error(status_code, params="Error method"):
        match status_code:
            case 401:
                status_code = status.HTTP_401_UNAUTHORIZED
        return Response(params, status_code)
    

