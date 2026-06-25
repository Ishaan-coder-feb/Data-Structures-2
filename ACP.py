std_profile=("Ishaan","9th grade","C","7 Subjects")
name=std_profile[0]
grade=std_profile[1]
section=[2]
no_of_sub=[-1]
print("Student name and grade is",std_profile[0:2])
mon_subs={"Math","English","Chemistry","Physics","Math"}
tue_subs={"Math","English","Biology","P.E",'Economics'}
mon_subs.add("Computer Science")
tue_subs.discard("P.E")
a=tue_subs.union(mon_subs)
b=tue_subs.intersection(mon_subs)
c=tue_subs.symmetric_difference(mon_subs)
d=mon_subs.difference(tue_subs)
print("The student profile is", std_profile)
print("His subjects on monday are ",mon_subs)
print("His subjects on tuesday are ",tue_subs)
print("The common subjects on both days are ",b)
print("Every subject he has is ",a)
print("Every subject present on monday but not on tuesday is ",d)
print("Every subject that is not common on both days is ",c)
