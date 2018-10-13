import random

from app.utils.file_util import get_members, get_last_solution, save_last_solution


def assign_pair(members, type=0):
    solution = []
    pair_num = 0
    if type == 2:
        members = delete_on_leveal_members(members)
        if len(members) == 0:
            return 'R U kidding me ?'
    if type == 0 or type == 2:
        return random_pair(members, pair_num, solution)
    elif type == 1:
        return special_pair(members, pair_num, solution)


def special_pair(members, pair_num, solution):
    members1 = members[0]
    members2 = members[1]
    while len(members1) > 0 and len(members2) > 0:
        a = extract_member(members1)
        b = extract_member(members2)
        if not check_assign(a, b):
            return False
        pair_num += 1
        solution.append([a, b])
    check_single_member(members1, pair_num, solution)
    check_single_member(members2, pair_num, solution)
    save_last_solution(solution)
    return solution


def random_pair(members, pair_num, solution):
    while (len(members) // 2) > 0:
        a = extract_member(members)
        b = extract_member(members)
        if not check_assign(a, b):
            return False
        pair_num += 1
        solution.append([a, b])
    check_single_member(members, pair_num, solution)
    save_last_solution(solution)
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
    last_solution = get_last_solution()
    for pair in last_solution:
        print(a,b,pair)
        if {a,b} == set(pair):
            print("++++++++++++++")
            return False
    return True
