def flatten(lst):
    aux_lst = []
    for elm in lst:
        if isinstance(elm, list):
            aux_lst += flatten(elm)
        else:
            aux_lst.append(elm)
    return aux_lst