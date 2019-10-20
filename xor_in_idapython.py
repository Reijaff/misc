start = read_selection_start()


def xor(size,key,buff):
    for index in range(0,size,8):
        curr_addr = buff+index
        temp = idc.get_qword(curr_addr) ^ key
        idc.patch_qword(curr_addr,temp)
