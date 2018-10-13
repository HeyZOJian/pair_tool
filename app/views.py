from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.service import *
from app.utils.file_util import add_members, delete_members, get_all_members

"""
                GET: 所有人随机分配
                POST:
                // 指定人员进行pair
                    {
                        "type": 0,
                        "members": ["A","B","C","D"]
                    }
                // 指定两个group进行pair
                    {
                        "type": 1,
                        "members": [["A","B","C","D"],["E","F","G"]]
                    }
                // 去除默认成员中的请假人员
                    {
                        "type":2,
                        "members":["amelia","carol"]
                    }
    """

@api_view(['GET','POST'])
def assign_pair_randomly(request):
    if request.method == 'GET':
        result = False
        while not result:
            result = assign_pair(get_members())
        return Response(result)
    elif request.method == 'POST':
        type = request.data.get("type")
        members = request.data.get('members')
        result = False
        while not result:
            result = assign_pair(members, type)
        return Response(result)

@api_view(['GET','PUT', 'DELETE'])
def user_view(request):
    if request.method == 'GET':
        return Response(get_all_members())
    elif request.method == 'PUT':
        print("======")
        members = request.data.get('members')
        if add_members(members):
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        members = request.data.get('members')
        delete_members(members)
        return Response(status=status.HTTP_200_OK)
