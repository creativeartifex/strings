course_name = "Python Programming"
print(len(course_name))
print(course_name[0])
print(course_name[0:3])
print(course_name[-1])
print(course_name[:])
print(course_name[:3])


# Escape Sequences
# \"
# \'
# \\
# \n

course_name = "Python \"Programming"
print(course_name)
course_name = "Python \'Programming"
print(course_name)
course_name = "Python \\Programming"
print(course_name)
course_name = "Python \nProgramming"
print(course_name)

# Formatted Strings
first = "Ahmed"
Last = "Zia"
full = first + " " + Last
print(full)

# another approach
full = f"{first} {Last}"
full = f"{len(first)} {Last}"
print(full)

full = f"{len(first)} {len(Last)}"
print(full)
full = f"{len(first)} {2+1}"
print(full)

# String Methods
course_name = "  Python Programming"
print(course_name.upper())
print(course_name.lower())
print(course_name.upper())
print(course_name.title())
print(course_name.strip())
print(course_name.find("Pyt"))  # index
print(course_name.replace("P", "j"))
print("Pro" in course_name)  # True
print("Ahmed" in course_name)  # False
print("Ahmed" not in course_name)
