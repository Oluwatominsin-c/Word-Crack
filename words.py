words = []
level1 = []
level2 = []
level3 = []
# CREATE OTHER LEVELS HERE


X = open('words.txt', 'r')
reader = X.readline()

# split all items in the file into words
while reader != "":
    words.append(reader.split(" - "))  # because of the ' - ' btwn words
    reader = X.readline()

X.close()

# remove all newline characters from words
for i in range(words.count(["\n"])):
    words.remove(["\n"])

# split items with "-" and appending it back to words
for i in words:
    for x in i:
        x = x.split("-")


for i in words:
    if len(i[0]) == 3:
        level1.append(i)
    if len(i[0]) == 4:
        level2.append(i)
    if len(i[0]) == 5:
        level3.append(i)
    # DO THESAME FOR OTHER LEVELS


def cracked(word_list):
    cracked = []
    i = 0
    while i < len(word_list):
        cracked.append(word_list[i][0])
        i += 1
    return cracked


def uncracked(word_list):
    uncracked = []
    i = 0
    while i < len(word_list):
        uncracked.append(word_list[i][1])
        i += 1
    return uncracked


l1cracked = cracked(level1)
l1uncracked = uncracked(level1)

l2cracked = cracked(level2)
l2uncracked = uncracked(level2)

l3cracked = cracked(level3)
l3uncracked = uncracked(level3)


# DO THIS FOR OTHER LEVELS

# print(l1uncracked)
