site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}


def dict_key_search(some_dictionary, target_key):
    if target_key in some_dictionary:
        return some_dictionary[target_key]

    for key in some_dictionary:
        if isinstance(some_dictionary[key], dict):
            result = dict_key_search(some_dictionary[key], target_key)
            if result:
                break
    else:
        return None
    return result


print(dict_key_search(site, 'h2'))
