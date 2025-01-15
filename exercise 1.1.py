# Duration avarage

other_courses_min = 2.5

other_courses_max = 7

other_courses_avarage = 4

dalto_course = 1.5

# Raw duration

avarage_raw = 5

dalto_avarage = 3.5

# Difference in duration

difference_with_min = 100 - dalto_course / other_courses_min * 100

difference_with_max = 100 - dalto_course * 1000 // other_courses_max / 10

difference_with_avarage = 100 - dalto_course / other_courses_avarage * 100

# Calculating the percentage of empty time removed

avarage_empty_time = 100 - other_courses_avarage * 1000 // avarage_raw / 10
dalto_empty_time = 100 - dalto_course * 1000 // avarage_raw / 10

# Showing time differences(exercisen A)

print("-------------------------------------------------------------------------------")

print("The Dalto course lasts: ")

print(f" - takes a {difference_with_min}% less time than the fastest one.")

print(f" - takes a {difference_with_max}% less time than the slowest one.")

print(f" - takes a {difference_with_avarage}% less time than the avarge.")

print("-------------------------------------------------------------------------------")

# Showing the empty spaces summarized(exercisen B)

print(f"An average course eliminates {avarage_empty_time}% of time")

print(f"An average course eliminates {avarage_empty_time}% of time")

print("-------------------------------------------------------------------------------")

# Seeing the difference if the courses lasted 10 hours

print(f"Watching ten hours in this course is equivalent to watching {other_courses_avarage * 100 // dalto_course / 10} of another courses")

print(f"Watching ten hours of other courses is equivalent to watching {dalto_course * 100 // other_courses_avarage / 10} of this courses")

print("-------------------------------------------------------------------------------")