katz_deli = []

def line(list):
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        print("The line is currently:", end="")
        for i in range(len(list)):
            print(f" {i+1}. {list[i]}",end="")
        print("")
    
def take_a_number(current_list:list, name:str):
    current_list.append(name)
    print(f"Welcome, {name}. You are number {len(current_list)} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else: 
        print(f"Currently serving {line.pop(0)}.")