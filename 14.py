def non_empty(get_pages):
    def wrapper():
        info_list = get_pages()

        for elem in info_list:
            if elem == '' or elem == None:
                info_list.remove(elem)

        return info_list

    return wrapper


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']


print(get_pages())
