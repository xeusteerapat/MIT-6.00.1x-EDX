def find_short(s):
    temp = s.split()
    empty = []
    for i in temp:
        empty.append(len(i))
    shortest = min(empty)
    return shortest  # l: shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))
