def create_board(num_place):
    if(num_place-1)%3 != 0:
        return ""
    space_count=num_place*2
    brace_space_count=0
    hyphen_count=1
    brace_string=""
    board=" "*space_count+" {}\n"
    for i in range(num_place-2):
        if hyphen_count%3==0:
            brace_string=" "*space_count+"{}"+"-"*(int((brace_space_count-1)/2))+"-{}"+"-"*(int((brace_space_count-1)/2))+"{}\n"
        else:
            brace_string=" "*space_count+"/"+" "*(int((brace_space_count/2)))+"|"+" "*(int((brace_space_count/2)))+"\\\n"
        board=board+brace_string
        space_count=space_count-1
        brace_space_count=brace_space_count+2
        hyphen_count=hyphen_count+1
    brace_string=" "*space_count+"{}"+"-"*(int((brace_space_count-1)/2))+"-{}"+"-"*(int((brace_space_count-1)/2))+"{}\n"
    board=board+brace_string
    return board