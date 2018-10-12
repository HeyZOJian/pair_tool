import random

from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET','POST'])
def assign_pair_randomly(request):
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

def get_members():
    return ['amelia', 'carol', 'chris', 'christy', 'corleone', 'dacoo', 'jo', 'nickey', 'vera', 'vito']


def assign_pair(members, type = 0):
    solution = dict()
    pair_num = 0
    if type == 2:
        members = delete_on_leveal_members(members)
        if len(members) == 0:
            return 'R U kidding me ?'
    if type == 0 or type == 2:
        return random_pair(members, pair_num, solution)
    elif type == 1:
        return special_pair(members, pair_num, solution)
    return solution


def special_pair(members, pair_num, solution):
    members1 = members[0]
    members2 = members[1]
    while len(members1) > 0 and len(members2) > 0:
        a = extract_member(members1)
        b = extract_member(members2)
        if not check_assign(a, b):
            return False
        pair_num += 1
        solution[pair_num] = (a, b)
    check_single_member(members1, pair_num, solution)
    check_single_member(members2, pair_num, solution)
    return solution


def random_pair(members, pair_num, solution):
    while (len(members) // 2) > 0:
        a = extract_member(members)
        b = extract_member(members)
        if not check_assign(a, b):
            return False
        pair_num += 1
        solution[pair_num] = (a, b)
    check_single_member(members, pair_num, solution)
    return solution


def delete_on_leveal_members(members):
    remain_members = get_members()
    for member in members:
        remain_members.remove(member)
    return remain_members


def check_single_member(members, pair_num, solution):
    if len(members) > 0:
        solution[pair_num + 1] = (members[0])


def extract_member(members):
    index = int(random.uniform(0, len(members)))
    member = members[index]
    members.remove(member)
    return member


def check_assign(a, b):
    if {'vito', 'amelia'} == {a, b}:
        print("woooooo")
        return False
    return True
