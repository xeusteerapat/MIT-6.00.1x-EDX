def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        return True
    elif int(pin) != 'int':
        return False
    else:
        return False
