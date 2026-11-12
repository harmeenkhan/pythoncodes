
"""

student={
    "name":"ayesha" ,
    "age":"41" ,
    "subject":"urdu" ,
    "marks":"90"
}
print(student.get("name"))

student_2={
    "age":"42"
}
student.update(student_2)
print(student)
student_3={
    "grade":"A"
}
student.update(student_3)
print(student)
student.pop("subject")
print(student)               """


"""

products={
    "bottle":2 ,
    "notebook":5 ,
    "totte bag":4 ,
} 
print(products)
prod1={
    "bottle":3 ,
    "laptop":6
}
products.update(prod1)
print(products)
products.pop("totte bag")
print(products)
products.get("notebook")
print(products.get("bottle", "no"))  """

"""
visitors={"Ali","Sara","Kashaf","Zaroon","Sara","Kashaf"}
print(visitors)
print(len(visitors))      """

#Realworld projects
product={"kurti":10 ,"kurta":8 ,"bag": 5 ,"pants":4 , "shirts":3 , "glassses":2}
print(product)

print(product.items())

if(product>5):
    print(products)