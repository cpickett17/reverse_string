user_Input = input("Enter a string")

#Extract each letter from the string
def Split(user_Input):
    return [letter for letter in user_Input]

#Store each letter in a list    
user_Input_List = Split(user_Input)

#Reverse the list
def Reverse(user_Input_List):
    return [char for char in reversed(user_Input_List)]
    
#Convert the reversed list into a new string    
reversed_String = ''.join(Reverse(user_Input_List))  

print(reversed_String)