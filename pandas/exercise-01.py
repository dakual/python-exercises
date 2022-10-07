import pandas as pd

student_dict = {'Name': ['Joe', 'Nat', 'Harry','Jack','Jose','Jill','Rose'],
                'Age': [20, 21, 19,17,18,19,17],
                'Marks': [85.10, 77.80, 91.54,72,87.9,90,72]}

# create DataFrame from dict
student_df = pd.DataFrame(student_dict)

# display first 5 rows
topRows = student_df.head()
print(topRows)