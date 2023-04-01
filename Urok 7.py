#my_list = [1, 2, 3]
#iterator = iter(my_list)

#for elem in iterator:
    #print(elem)

def raise_to_the_degrees(number, max_degree):
    i=0
    for _ in range(max_degree):
        yield number**i
        i+=1

res = raise_to_the_degrees(122345, 500)
print(res)
for _ in res:
    print(_)

#class Helper:
    #def __init__(self, work):
        #self.work = work
    #def __call__(self, work):
        #return f"I will help you with your {self.work}. Afterwards I will help you with {work}"

#helper = Helper("homework")
#print(helper("cleaning"))