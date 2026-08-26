marks={
  "eng":67,
  "hindi":89,
  "science":55
}

list=[]
for value in marks.values():
     list.append(value)


sum_of_marks=sum(list)
no_of_items=len(marks)
avg=sum_of_marks / no_of_items
print(avg)