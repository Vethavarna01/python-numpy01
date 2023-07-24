#computaions using numpy functions
#(a)
import numpy as np

lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(arr)

#(b)
import numpy as np

lst = [1, 2, 3, 4, 5]
tupl = (6, 7, 8, 9, 10)

array_from_list = np.array(lst)
array_from_tuple = np.array(tupl)

print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)

#data manipulations using pandas
#(a)
import numpy as np
import pandas as pd

arr= np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
series_1 = pd.Series([10, 11, 12, 13, 14])

df_from_array = pd.DataFrame(arr, columns=['A', 'B', 'C'])

df_from_series = pd.DataFrame(series_1, columns=['Values'])

print("DataFrame from NumPy array:")
print(df_from_array)

print("DataFrame from Pandas Series:")
print(df_from_series)


#(b)
import pandas as pd

series_1 = pd.Series([10, 20, 30, 40, 50])
series_2 = pd.Series([5, 10, 15, 20, 25])

# Additiom
addition_result = series_1 + series_2

# Subtraction
subtraction_result = series_1 - series_2

# Multiplication
multiplication_result = series_1 * series_2

# Division
division_result = series_1 / series_2

print("Addition Result:")
print(addition_result)

print("Subtraction Result:")
print(subtraction_result)

print("Multiplication Result:")
print(multiplication_result)

print("Division Result:")
print(division_result)


#(c)
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 24],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 52000],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT']
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Rows where age is greater than 25:")
filtered_df = df[df['Age'] > 25]
print(filtered_df)

print("Selecting Name and Salary columns:")
selected_columns = df[['Name', 'Salary']]
print(selected_columns)

df['Bonus'] = df['Salary'] * 0.05
print("DataFrame with the Bonus column:")
print(df)

grouped_df = df.groupby('Department')['Salary'].mean()
print("Average salary by department:")
print(grouped_df)

sorted_df = df.sort_values(by='Salary', ascending=False)
print("DataFrame sorted by Salary:")
print(sorted_df)
