#swap case
#1
a=5
b=10
a,b=b,a
print(a,b)

#2
i="python"
def swap_case(string):
    new_string=""
    for i in string:
        if i.isupper():
            new_string+=i.lower()
        else:
            new_string+=i.upper()
    return new_string
print(swap_case("python"))

#3
print("python".swapcase())