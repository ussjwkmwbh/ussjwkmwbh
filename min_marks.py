max_marks_pt = 40
max_marks_hy = 70

pt1_marks=40
hy_marks=70
pt2_marks=40

percent_added_by_pt = 10
percent_added_by_hy = 30

percentage_yet_obtained = (pt1_marks/max_marks_pt)*percent_added_by_pt + (hy_marks/max_marks_hy)*percent_added_by_hy + (pt2_marks/max_marks_pt)*percent_added_by_pt
percentage_needed = 33 - percentage_yet_obtained
marks_needed_in_final = percentage_needed *(8/5)
print("Marks needed in final exam to pass: ",marks_needed_in_final)
print("Percentage obtained so far: ",percentage_yet_obtained)
