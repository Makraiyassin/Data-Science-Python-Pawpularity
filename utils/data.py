import pandas as pd

data = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
sample = pd.read_csv('sample_submission.csv')

populary= data[data['Pawpularity'] > 75]
unpopulary= data[data['Pawpularity'] < 25]

count_populary = {column:populary[column].value_counts() for column in populary.columns if not column == "Pawpularity" and not column == "Id"}
count_unpopulary = {column:unpopulary[column].value_counts() for column in unpopulary.columns if not column == "Pawpularity" and not column == "Id"}

df_populary = pd.DataFrame([[value,count_populary[value][1],count_populary[value][0]] for value in count_populary],columns=["Criterion","Yes","No"])
df_unpopulary = pd.DataFrame([[value,count_unpopulary[value][1],count_unpopulary[value][0]] for value in count_unpopulary],columns=["Criterion","Yes","No"])

# print(df_populary)

# print(data[(data['Subject Focus']==1) & (data['Pawpularity'] > 50)] )
# print(data[data["Pawpularity"] < 25])
# print(data[data["Pawpularity"] > 75])
# print(data['Pawpularity'].value_counts())

