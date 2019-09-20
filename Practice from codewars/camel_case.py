def camel_case(string):
    return "".join([x.title() for x in string.split(" ")])


camel_case("camel case method")
