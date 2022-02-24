string='johnmarkmmarkpeter'
find_string='mmarks'
replace_string='fictional'

def finds(s, sub):
    idx = 0
    
    while idx < len(s):
        #print("test")
        if s[idx:idx+len(sub)] == sub:
            print(s[idx:len(sub)])
            return idx
        idx=idx+1
    return -1


def replace(s,sub_find,sub_replace):
    if finds(s,sub_find)!= -1:
        start_index= finds(s,sub_find)
        end_index= start_index+len(sub_find)
        return (s[0:start_index]+sub_replace+s[end_index:])
    return -1
    
print(replace(string,find_string,replace_string))

