list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer={list1[i]:list2[i] for i in range(3)}
print(answer)

#method second
answer2=dict(zip(list1,list2))
print(answer2)