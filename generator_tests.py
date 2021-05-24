

def liczby():
    for i in range(11):
        yield i * 2
        
gen = liczby()     

for i in range(5):
    res = next(gen)
    print(res)
    
print("----")


for i in liczby():
    print(i)