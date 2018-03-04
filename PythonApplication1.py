'''student=['666','555','mail']
print(student[-1])
student.append('51zxw')
print(student)
student.insert(0,'hello')
print(student)
student.pop (1)
print(student)

#元组(tuple)        
course=('chinese','English','math','computer')
print(course)
print(course[-1])
print(course[1:3])
print(course[:2])

print(len(course))

score=(99,66,55,84,78,64,99)
print(max(score))
print(min(score))

#python字典
student={1:'jack',2:'bob',3:'marry',4:'micle' }
print(student[3])

student[5]='huqiao'
print(student)

student[2]='Harry'
print(student)

del student[2]
print(student)

student.clear()
print(student)

del student
print(student)'''
#条件判断
score=100
if score>=80:
    print("score is A")
elif score>=60:
    print("score is B")
else:
    print("score is C")
#循环语句
student=['jack','bob','marry','micle']
for stu in student:
    print(stu)
sum=0
for i in range(11):
    sum+=i
print(sum)

n=10
while n>0:
    n-=1
    print(n)
print("over!")