import  numpy as np

arr=np.arange(10).reshape(2,5)
print(arr)
print(arr.shape)
print(arr.dtype.name)
print(arr.itemsize)
print(type(arr))
a=np.array([2,3,4,5])
print(a)
print("two dimansional")
b=np.array([(1,2,4),(6,7,8)])
print(b)
_3d=np.array([(10,20),(20,40),(30,60)])
print(_3d)
complex = np.array([[1,2],[3,4]],dtype=complex)
print(complex)
print("index  ")
print(complex[[0]])
zero=np.zeros((3,4))
print(zero)
print("fill with one")
one=np.ones((2,3,4),dtype=np.int32)
print(one)
empty=np.empty((2,3,4))
print("empty ",empty)
print("range")
range=np.arange(10,40,1)
print("Range = ",range)
#pi import
from numpy import pi
print("linespace ",np.linspace(0,2,9))
x=np.linspace(0,2.0*pi,100)
print("X== ", x)

f=np.sin(x)
print("sin = ",f)

print("basic operation of numpy ")

xx=np.arange(4)
yy=np.array([20,30,40,50])
print("xx+yy = " ,xx+yy)
x=10.0*np.sin(xx)
print(x)

print(x<55)

print(np.arange(100000))
print(np.arange(1000000).reshape(1000,1000))
