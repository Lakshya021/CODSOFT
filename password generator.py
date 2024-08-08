import random
length=int(input("Enter required length for password = "))
alp_num_sym=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '/','1','2','3','4','5','6','7','8','9','0']
pass_list=[]
password=""
for i in range(1,length+1):
    pass_list+=random.choice(alp_num_sym)
random.shuffle(pass_list)
for j in pass_list:
    password+=j
print(password)