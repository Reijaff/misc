
pattern = "0F 05"

newarr = []
addr = idc.get_inf_attr(INF_MIN_EA)
while addr !=idc.get_inf_attr(INF_MAX_EA):
    addr = idc.find_binary(addr, SEARCH_NEXT|SEARCH_DOWN, pattern)
    if addr != idc.BADADDR:
        print hex(addr)
        newarr.append(hex(addr))