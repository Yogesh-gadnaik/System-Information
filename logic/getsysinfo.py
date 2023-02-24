from model.dictinory import init_dictionary


def sys_name(info):
    sys_info = init_dictionary()
    try:
        if info == "allinfo":
            return sys_info

        else:
            return sys_info[info], info

    except Exception as e:
        e = "Please select proper option"
        return e
