import requests
import string
import time
import threading
import logging

f = open("available.txt", "w")
f.close() 

f = open("available.txt", "a")

lista = []
abc = list(string.ascii_lowercase)
for w in range(0, 10):
    abc.append(str(w))
print(abc)
abc.append("_")
abc.append("-")

def urlChecker(link:str):
    req = requests.get(link)
    cont = str(req.content)
    #The specified profile could not be found.
    #No group could be retrieved for the given URL.
    if "The specified profile could not be found." in cont:
        return True
    else:
        return False


def validUrlNum(size: int):
    """
    Creates a list of possible valid numbered urls with all combinations possible with the desired number char length.
    Min: 2 chars.
    Max: 32

    Args:
        size (int): Number of chars wanted.

    Returns:
        list: possible numbers
    """
    lista = []
    if size <= 2:
        lista += [
        format(num, "0" + str(2))
        for num in range(10**2)
        if format(num, "0" + str(2)) not in lista
        ]
    else:
        lista += [
            format(num, "0" + str(size))
            for num in range(10**size)
            if format(num, "0" + str(size)) not in lista
        ]
    return lista


for x in validUrlNum(4):
    link = f"https://steamcommunity.com/groups/{x}"    
    print(link)
    if urlChecker(link):
        print(f"FOUND! {x}")
        lista.append(link)
        f.write(link)
    f.close()


# print(
#     "There are "
#     + str((38 * 38 * 38) - (26 * 26 * 26) - (10 * 10 * 10))
#     + " possibilities"
# )


# with open('ids.txt', 'w') as f:
#     for x in abc:
#         for y in abc:
#             for z in abc:
#                 if x in list(string.ascii_lowercase) and y in list(string.ascii_lowercase) and z in list(string.ascii_lowercase):
#                     None
#                 elif x in [str(f) for f in range(10)] and y in [str(f) for f in range(10)] and z in [str(f) for f in range(10)]:
#                     None
#                 else:
#                     req = requests.get(f"https://steamcommunity.com/id/{x+y+z}")
#                     cont = str(req.content)
#                     print(f"Analizing https://steamcommunity.com/id/{x+y+z}")
#                     if "The specified profile could not be found." in cont:
#                         f.write(f"https://steamcommunity.com/id/{x+y+z}")
#                         f.write('\n')
#                         print(f"FOUND! {x+y+z}")

################################ Atual #######################################
# for x in range(2,33):
#     for y in range(0,10):
#             req = requests.get(f"https://steamcommunity.com/groups/{x*str(y)}")
#             cont = str(req.content)
#             print(f"Analizing https://steamcommunity.com/groups/{x*str(y)}")
#             if "No group could be retrieved for the given URL." in cont:
#                 print(f"FOUND! {x*str(y)}")
#                 lista.append(f"https://steamcommunity.com/groups/{x*str(y)}")
#                 f = open("available.txt", "a")
#                 f.write(f"https://steamcommunity.com/groups/{x*str(y)}")

# print(lista)
# f.close()

# with open('groups.txt', 'w') as f:
#     for x in abc:
#         for y in abc:
#             for z in abc:
#                 if x in list(string.ascii_lowercase) and y in list(string.ascii_lowercase) and z in list(string.ascii_lowercase):
#                     None
#                 elif x in [str(f) for f in range(10)] and y in [str(f) for f in range(10)] and z in [str(f) for f in range(10)]:
#                     None
#                 else:
#                     req = requests.get(f"https://steamcommunity.com/groups/{x+y+z}")
#                     cont = str(req.content)
#                     print(f"Analizing https://steamcommunity.com/groups/{x+y+z}")
#                     if "No group could be retrieved for the given URL." in cont:
#                             f.write(f"https://steamcommunity.com/groups/{x+y+z}")
#                             f.write('\n')
#                             print(f"FOUND! {x+y+z}")

# for i in lista3:
#     req = requests.get(f"https://steamcommunity.com/groups/{i}")
#     cont = str(req.content)
#     print(f"Analizing https://steamcommunity.com/groups/{i}")
#     if "No group could be retrieved for the given URL." in cont:
#         lista.append(i)
#         print(i)
# print([str(f) for f in range(10)])
# for x in abc:
#     for y in abc:
#         for z in abc:
#             if x in list(string.ascii_lowercase) and y in list(string.ascii_lowercase) and z in list(string.ascii_lowercase):
#                 None
#             elif x in [str(f) for f in range(10)] and y in [str(f) for f in range(10)] and z in [str(f) for f in range(10)]:
#                 None
#             elif "-" not in x+y+z and "_" not in x+y+z:
#                 None
#             else:
#                 req = requests.get(f"https://steamcommunity.com/id/{x+y+z}")
#                 cont = str(req.content)
#                 print(f"Analizing https://steamcommunity.com/id/{x+y+z}")
#                 if "The specified profile could not be found." in cont:
#                     lista.append(f"https://steamcommunity.com/id/{x+y+z}")
#                     print(f"https://steamcommunity.com/id/{x+y+z}")

# for x in abc:
#     for y in abc:
#         for z in abc:
#             req = requests.get(f"https://steamcommunity.com/groups/{x+y+z}")
#             cont = str(req.content)
#             print(f"Analizing {x+y+z}")
#             if "No group could be retrieved for the given URL." in cont:
#                 lista.append(x+y+z)
#                 print(x+y+z)
