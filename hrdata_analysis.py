import pandas as pd
df = pd.read_csv('HR Data.csv')
df.describe()

columns_required = ['Age','Department','Education','EmployeeNumber','JobInvolvement','JobRole','MonthlyIncome','YearsAtCompany','YearsInCurrentRole','YearsSinceLastPromotion']
df = df[columns_required]
print("Data After removing unnecessary columns")
df.head()

renaming_columns = {
    'EmployeeNumber': 'Employee Id',
    'JobInvolvment' : 'Job Participation'
    }
df.rename(columns=renaming_columns, inplace=True)
df.columns

df.drop_duplicates(inplace=True)
print("Eliminating Redundancy entites")
df.head()

print("Drop rows with any NaN values")
df.dropna(inplace=True)
df.head()