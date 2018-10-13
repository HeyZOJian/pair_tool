import json

from app.config import members_info_path, history_path


def get_members():
    last_solution = get_last_solution()
    if last_solution:
        members = [[],[]]
        members[0] = [pair[0] for pair in last_solution]
        members[1] = [pair[1] for pair in last_solution if len(pair)>1]
        return members
    else:
        f = open(members_info_path, 'r')
        members = list(json.load(f)['members'])
        return [members[:7], members[7:]]

def add_members(new_members):
    flag = False
    json_data = dict()
    json_data['members'] = list(get_members())
    for new_member in new_members:
        if new_member not in json_data['members']:
            flag = True
            json_data['members'].append(new_member)
    f = open(members_info_path, 'w')
    f.write(json.dumps(json_data))
    f.close()
    return flag

def delete_members(delete_members):
    json_data = dict()
    json_data['members'] = list(get_members())
    print(json_data['members'])
    for delete_member in delete_members:
        if delete_member in json_data['members']:
             json_data['members'].remove(delete_member)
    f = open(members_info_path, 'w')
    f.write(json.dumps(json_data))
    f.close()

def save_last_solution(solution):
    f = open(history_path, 'w')
    json_data = dict()
    json_data['last_solution'] = solution
    f.write(json.dumps(json_data))
    f.close()

def get_last_solution():
    f = open(history_path,'r')
    if f is not None:
        return list(json.load(f)['last_solution'])
    return None

if __name__ == "__main__":
    print(get_last_solution())
    # add_members(["Vito",])
    # delete_members(["Vito",])
