def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)

    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def separate_into_vip_and_regular(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip_guest(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return sorted(vip_guests), sorted(regular_guests)


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guests) = separate_into_vip_and_regular(guests)

    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)



guest_count = int(input())
reservations = input_to_list(guest_count)
guest_arrived = input_to_list_until_command("END")
guest_not_arrived = set(reservations).difference(guest_arrived)
print_result(guest_not_arrived)
