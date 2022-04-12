
# This function removes character duplicates and creates a new sorted string 
msting='monty pythons flying circus'
duplicates = []
tstring = ""
def no_duplicates(msting):

    tstring = ""
    for i in msting :
        if i not in tstring and i != " " :
            tstring=tstring + i
    sortlist = sorted(tstring)
    print("".join(sortlist))




# A function that creates a list from the string in reverse order  
def reversed_words(msting):
    tlist = msting.split(" ")
    tlist=tlist[::-1]
    print(tlist)


# A function that creates a list and adds an element to the list every 4 characters 
def four_char_strings(msting):

    print([msting[i:i+4] for i in range(0,len(msting),4)])







def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']



no_duplicates(msting)
print("")
reversed_words(msting)
print("")
four_char_strings(msting)
