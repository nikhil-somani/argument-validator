import itertools

def implies (a, b):
    return (not a) or b

def and_func(*args):
    output = True
    for n in args:
        output = output and n
    return output

def or_func(*res):
    result = False
    for i in res:
        result = result or i
    return result


#statement in the form of propositions

# print("p->q ^ r ->s")
# print (" P Q R P->Q R->S PREMISE 1")

for (P,Q,R,S,T) in itertools.product([True,False],repeat=5):
    print ("{:2d}".format(P),end="")
    print ("{:2d}".format(Q),end="")
    print ("{:2d}".format(R),end="")
    print ("{:2d}".format(S),end="")
    print ("{:2d}".format(T),end="")

    print ("{:2d}".format(implies(P,Q)),end="")
    print ("{:2d}".format(implies(R,S)),end="")
    print ("{:2d}".format(and_func(Q,S)),end="")
   
    print ("{:2d}".format(and_func(implies(P,Q), implies(R,S))),end="")
    print ("{:2d}".format(implies(and_func(Q,S),T)),end="")
    print("{:2d}".format(not(T)), end="")
    print ("{:2d}".format(and_func(and_func(implies(P,Q), implies(R,S)), implies(and_func(Q,S),T), not(T) )),end="")

    print("")