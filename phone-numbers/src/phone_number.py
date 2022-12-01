
def create_phone_number(integer):
    number_string = str(integer)
    if len(number_string) == 10:
        part1 = number_string[0:3]
        part2 = number_string[3:6]
        part3 = number_string[6:10]
        return f'({part1}) {part2}-{part3}'
    return False
