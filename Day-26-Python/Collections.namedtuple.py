# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
num_students, Student = int(input()), namedtuple('Student', input())
student_list = [Student(*input().split()) for _ in range(num_students)]
print(f"{sum(float(s.MARKS) for s in student_list) / num_students:.2f}")

