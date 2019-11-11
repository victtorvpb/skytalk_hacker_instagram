from rest_framework.decorators import api_view
from rest_framework.response import Response
from instagram_private_api import Client

@api_view(['GET'])
def its_alive(request):
    return Response({'message': 'its_alive'})

@api_view(['GET'])
def instagram_data(request):
    try:
        username = 'marketingran'
        password = 'a123b456c789z'
        api = Client(username, password)
        
        username_param = request.query_params.get('username')
        if not username_param:
            return Response({})

        result_search_user = api.search_users(username_param)

        if not result_search_user.get('users'):
            return Response({})
        

        pk_user = result_search_user.get('users')[0].get('pk')

        result = api.user_detail_info(pk_user)
        return Response(result)
    except:
        return Response({'error':'error'}, status=404)