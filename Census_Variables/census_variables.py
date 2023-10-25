import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())
#print(census.dtypes)

census['birth_year'] = census['birth_year'].replace(['missing'],1967)
print(census.birth_year.unique())

census['birth_year'] = census['birth_year'].astype("int")
# print(census.dtypes)
# print(census.birth_year.mean())

census['higher_tax'] = pd.Categorical(census['higher_tax'],['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered = True)
#print(census.higher_tax.unique())
census['higher_tax'] = census['higher_tax'].cat.codes
#print(census.head())
print(census['higher_tax'].median())

#OHE martial_status to create binary variables of each category
# census = pd.get_dummies(data = census, columns=['marital_status'])

#create new variable marital_codes by label encoding marital_status
census['marital_codes'] = pd.Categorical(census['marital_status'])
census['marital_codes'] = census['marital_codes'].cat.codes

#determine age
census['age'] = 2023 - census['birth_year']
#determine range of age groups with five-year increments
age_group_ranges = range(census['age'].min(), census['age'].max() +1, 5)
#map birth year to age group
def map_age_groups(age):
  for start_age in age_group_ranges:
    end_age = start_age + 4
    age_group = f"{start_age}-{end_age}"
    if start_age <= age <= end_age:
      return age_group
#create age_group column by apply the mapping function
census['age_group'] = census['age'].apply(map_age_groups)
#turn categorical and label encode
census['age_group_cat'] = pd.Categorical(census['age_group'], ordered = True)
census['age_group_cat'] = census['age_group_cat'].cat.codes
print(census.head())