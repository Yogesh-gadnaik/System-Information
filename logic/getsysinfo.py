from model.dictinory import init_dictionary


def sys_name(info):
    sys_info = init_dictionary()
    try:
        if info == "allinfo":
            dict = {}
            for i, j in sys_info.items():
                dict[i] = j
            return dict

        else:
            return sys_info[info], info

    except Exception as e:
        e = "Please select proper option"
        return e
