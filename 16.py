import random
import datetime


def create_groups():
    teams = [i for i in range(1, 17)]
    random.shuffle(teams)

    return [teams[i: i + 4] for i in range(0, 13, 4)]


def print_groups_tour(groups):
    for i in range(4):
        print(f"Group{i + 1}")
        print(*groups[i])
    print()


def print_caledar(groups):
    shuf = ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2))

    date = datetime.datetime(2022, 9, 14, 22, 45)
    two_week = datetime.timedelta(weeks=2)

    for i in range(3):
        print(date.strftime("%d/%m/%Y,%H:%M"))
        for j in range(4):
            print(f"Group{j + 1}")
            for k in range(0, 3, 2):
                print(f"{groups[j][shuf[i][k]]} vs {groups[j][shuf[i][k + 1]]}")
        print()


groups = create_groups()
print_groups_tour(groups)

print_caledar(groups)