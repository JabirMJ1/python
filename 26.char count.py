stri = "My name is Jabir"
list_str = list(stri)
c=0
for i in list_str:
    c = 0
    if i!=" ":
        for j in range(0, len(list_str)):
            if i == list_str[j]:
                c = c + 1
                list_str[j]=" "
        print(f"{i} = {c}")

