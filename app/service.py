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
        return random_pair(get_members(), pair_num, solution)
    elif type == 1:
        return random_pair(members, pair_num, solution)


def random_pair(members, pair_num, solution):
    members1 = members[0]
    members2 = members[1]
    while len(members1) > 0 and len(members2) > 0:
        a = extract_member(members1)
        b = extract_member(members2)
        print("===",a,b)
        if not check_assign(a, b):
            return False
        pair_num += 1
        solution.append([a, b])
    check_single_member(members1, pair_num, solution)
    check_single_member(members2, pair_num, solution)
    save_last_solution(solution)
    return solution

def delete_on_leveal_members(members):
    remain_members = get_members()
    for member in members:
        remain_members.remove(member)
    return remain_members


def check_single_member(members, pair_num, solution):
    if len(members) > 0:
        solution.append(members[0])


def extract_member(members):
    index = int(random.uniform(0, len(members)))
    member = members[index]
    members.remove(member)
    return member


def all_ITA(a, b):
    ITA = ['Vito','Amelia','Jeffery','Quinn']
    if a in ITA and b in ITA:
        print(a, b)
        return False
    return True


def check_assign(a, b):
    if not all_ITA(a,b):
        return False
    last_solution = get_last_solution()
    if last_solution is not None:
        for pair in last_solution:
            if {a,b} == set(pair):
                return False
    return True
