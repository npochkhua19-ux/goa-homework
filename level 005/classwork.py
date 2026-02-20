# გაასწორე კოდი ისე რომ არ გამოიწვიოს error 
# ag = "15"
# height = "170.5"

# print(age + 5)
# print(height + 10)

# დავალება 2)
# მომხმარებელს შეამოატანინე 2 რიცხვი ინფუთით და შემდეგ შეადარე თუ რომელია უფრო მეტი

#1
age="15"
age=int(age)
height="170.5"
height=float(height)
print(age+5)
print(height+10)
#2
a=int(input("sheiyvaen ricxi :"))
b=int(input("sheiyvane ricxvi :"))
print(a>b)

# შექმენი ცვლადი სადაც შეინახავ ინტეჯერ მონაცემთა ტიპს და შემდეგ შეეცადე რომ კონკატინაცია მოახდინო მაგასა და სტრინგს შორის რატომ გამოიწყვია error და შემდეგ გამოასწორე 
d=12
g="ricxvi"
g=int(g)

print(d+g)