#anagrams
def chk(in_str,in_list):
    out_list=[]
    str=in_str
    in_word=list(str)
    in_word.sort()
    for i in range(len(in_list)):
        x=in_list[i]
        x_list=list(x)
        x_list.sort()
        if x_list==in_word:
            out_list.append(x)
    return out_list
