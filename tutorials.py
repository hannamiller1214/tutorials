#Check an array of emails
def email_checker(add):
    add_arr = add.split("@")
    return add_arr[1] == "gmail.com"

email_checker = email_checker("hm@gmail.com")
print(email_checker)

#Addition Example
arr=[10, 25, 3, -5, -10]

def sum_greater_than_one_hundred(arr):
    sum = 0
    for x in arr:
        sum = sum + x
    if sum > 100:
        return sum
    else:
        return False

#Reverse a string
def reverse_str(str):
    reverse_string = []
    for char in str:
        reverse_string.insert(0, char)
    reverse_string = "".join(reverse_string)
    return reverse_string

print(reverse_str("Denise Hiatt"))
