def find_short(s):
    temp = s.split()
    empty = []
    for i in temp:
        empty.append(len(i))
    l = min(empty)
    return l  # l: shortest word length


print(find_short("bitcoin take over the world maybe who knows perhaps"))
