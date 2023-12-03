def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return ["Hello, {}! You'll be assigned to room {}!".format(name, index + 1) for index, name in enumerate(names)]

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)

    for room in rooms:
        print(room)

names_list = ["Arel", "Carol"]
printer(names_list)
