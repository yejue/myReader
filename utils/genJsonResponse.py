from utils.res_code import error_map, Code


def json_response(errno=Code.OK, errmsg=error_map[Code.OK], data=None, kwargs=None):
    json_dict = {
        "errno": errno,
        "errmsg": errmsg,
        "data": data
    }

    if kwargs and isinstance(kwargs, dict):
        json_dict.update(kwargs)

    return json_dict
