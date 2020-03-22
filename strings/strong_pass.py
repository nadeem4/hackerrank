numbers = list("0123456789")
lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = list("!@#$%^&*()-+")

n = int(input())
s = str(input())

rule_dict = dict()

rule_dict['digit'] = 0
rule_dict['lower_case'] = 0
rule_dict['upper_case'] = 0
rule_dict['special_char'] = 0

len_of_s = len(s)

for char in list(s):
    if char in numbers:
        rule_dict['digit'] += 1
    if char in lower_case:
        rule_dict['lower_case'] += 1
    if char in upper_case:
        rule_dict['upper_case'] += 1
    if char in special_characters:
        rule_dict['special_char'] += 1

req_count = 0
if rule_dict['digit'] == 0:
    req_count+=1

if rule_dict['lower_case'] == 0:
    req_count+=1
    
if rule_dict['upper_case'] == 0:
    req_count+=1

if rule_dict['special_char'] == 0:
    req_count+=1

#print(rule_dict)
if  len_of_s < 6 and req_count <  6 -len_of_s:
    print(6- len_of_s)
else:
    print(req_count)


        
