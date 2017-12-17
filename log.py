def exception(message):
    print(message)
    raise Exception


def exceptions(array, title):
    for element in array:
        print(title, element)
    raise Exception
