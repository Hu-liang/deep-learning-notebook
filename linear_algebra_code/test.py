#coding:utf-8

from Vector import Vector


# #my_vector = Vector([1,2,3])
# my_vector = Vector(['1','2','3'])
# print my_vector
# #my_vector2 = Vector([1.23123,2.03131,3.87598])
# my_vector2 = Vector(['1.23123','2.03131','3.87598'])
# my_vector3 = Vector([1,2,4])

# print my_vector == my_vector2
# print my_vector3 == my_vector

# print my_vector.plus(my_vector2)
# print my_vector.minus(my_vector3)
# print my_vector.times_scalar(3)



v = Vector(['7.887','4.138'])
w = Vector(['-8.802','6.776'])
print v.dot(w)

v = Vector(['7.35','0.221','5.188'])
w = Vector(['2.751','8.259','3.985'])
print v.angle_with(w,in_degrees=True)