# Duration avarage

other_courses_min = 2.5

other_courses_max = 7

other_courses_avarage = 4

dalto_course = 1.5

# Raw duration



# Difference in duration

difference_with_min = 100 - dalto_course / other_courses_min * 100

print(f"Dalto's course takes {difference_with_min}% less than the fastest course")

difference_with_max = 100 - dalto_course * 1000 // other_courses_max / 10

print(f"Dalto's course takes {difference_with_max}% less than the slowest course")

difference_with_avarage = 100 - dalto_course / other_courses_avarage * 100

print(f"Dalto's course takes {difference_with_avarage}% less than the avarage")