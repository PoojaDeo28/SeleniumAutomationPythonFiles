class A:    pass
class Z:    pass
class Y:    pass
class X(Z,Y):    pass
class B(A):    pass
class C(X,B):    pass
class E(B):    pass
class P(C):    pass
class Q(C):    pass
class G(E):    pass
class F(E):    pass


#print(A.mro())

#print(B.mro())

#print(Z.mro())

#print(Y.mro())

#print(X.mro())

#print(C.mro())

#print(E.mro())

#print(P.mro())

#print(Q.mro())

print(G.mro())

print(F.mro())

