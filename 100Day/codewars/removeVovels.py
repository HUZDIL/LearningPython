
#passed
def disemvowel(string_):
    a=""
    for i in string_:
        if i not in "AEIİOÖUÜaeıioöuü":
            a +=i
        else:
            continue

    return  a


string_ = "This website is for losers LOL!"

print(disemvowel(string_))


