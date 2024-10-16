# "while" loop, loops contain from 2 operations ("itr", "next")

# while условие:
#     блок кода пока условие True


# num = 5
# count = 0
# while count < 10:
#     count += 1
#     print(count)  


# password = "12345"

# user_input = input("Enter a password: ")
# while True:
#     if user_input == password:
#         print("Correct")
#         break
#     else:
#         print("Not correct, try again")
#         user_input = input("Enter a password: ") 


# password = "12345"
# flag = True

# user_input = input("Enter a password: ")
# while flag:
#     if user_input == password:
#         print("Correct")
#         flag = False
#     else:
#         print("Not correct, try again")
#         user_input = input("Enter a password: ") 
# else:
#     print("hello") 



# continue 

# count = 0

# while count < 10: 
#     count += 1
#     if count == 5:
#         continue
#     print(count) 




# num = int(input("Enter a num: "))
# total = 0
# while num != 0:
#     total += num
#     num = int(input("Enter a num: ")) 
# print("Sum is: ", total) 
     
 
# num = int(input("Enter a num: "))
# for i in range(num, 0, -1):
#     print(i) 


# count = 0
# total = 0
# numbers = float(input("Enter numbers: "))
# while numbers != 0:
#     numbers = float(input("Enter numbers: "))
#     if numbers == 0:
#         break
#     total += numbers
#     count += 1
# if count > 0:
#     a_a = total / count
#     print("Avarage is ", a_a)


# pin = "1323"
# count = 0
# while count < 3:
#     user_input = input("Enter a PIN: ")
#     if user_input == pin: 
#         print("Correct!")
#         break
#     else:  
#         count += 1
#         print(f"not correct, you have {3 - count} attemps left!")
# if count == 3:
#     print("You have no attempts left! Sorry...")




