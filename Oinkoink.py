oink = str(input())
split = oink.split()
vowel = ("a",'e','i','o',"u")
consonant = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
for x in split:
    if x[0] == vowel:
        x += ("way")
    while x[0] == consonant:
        x += x[0]
        x.replace(x[0],'')

print (' '.join(split))