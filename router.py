# связь между view и data base

from view import *
from database import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            name = get_name()
            res_str = write_name(name)
            print_info(res_str)
        elif ans in [2, 3, 4]:
            char = get_some_info()
            full_lst, accept_lst, res_str = searh_name(char)
            print_info(accept_lst, res_str)
        if ans == 3 or ans == 4:
            selected_num = select_name()
            new_line = None
        if ans == 4:
            new_line = get_name()
            res_str = change_name(full_lst, accept_lst[selected_num], new_line)
            print_info(res_str)
        elif ans == 5:
            res_str = get_all()
            print_info(res_str)
        elif ans == 6:
            break
        
main()

    