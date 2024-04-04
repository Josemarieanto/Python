##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##print(x)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##y = x.get("Age")
##print(y)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##y = x.items()
##print(y)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##y = x.keys()
##print(y)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##y = x.pop("Qualification")
##print(y)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##y = x.setdefault("Age" , "21")
##print(y)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##x.update({"Course" : "python"})
##print(x)
##x = {
##    "Name" : "josemarie",
##    "Age" : "21",
##    "Qualification" : "B.Com"
##}
##x.clear()
##print(x)
##x = ('key1', 'key2', 'key3')
##y = 1
##
##z = dict.fromkeys(x, y)
##
##print(z)
user_input = input("username : ")
user_dict = {user_input}
letter_count = {}
for i in user_input:
    if i in letter_count:
        letter_count[i] += 1
    else:    
        letter_count[i] = 1
print(letter_count) 












