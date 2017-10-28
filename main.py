source_ticket = "103394428%rp%%11%26"


def get_num(ticket):

    stack = [0, 0, 8, 6, 4, 2, 3, 5, 9, 7, 0, 0, 0]
    x = 0
    for num in range(13):
        x += stack[num] * int(ticket[num])
    y = 11 - (x % 11)
    if y == 11:
        return '5'
    if y == 10:
        return '0'
    return str(y)


for i in range(10):

    place = get_num(
        source_ticket.replace(
            "%rp%",
            str(i)).replace(
            "%11%",
            str(0)))

    print(source_ticket.replace("%rp%", str(i)).replace("%11%", place))
