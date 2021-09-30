import pandas as pd

data = pd.read_csv('./train.csv')
# test = pd.read_csv('test.csv')
# sample = pd.read_csv('sample_submission.csv')

populary= data[data['Pawpularity'] > 75]
count_populary = {column:populary[column].value_counts() for column in populary.columns if not column == "Pawpularity" and not column == "Id"}
df_populary = pd.DataFrame([[value,count_populary[value][1],count_populary[value][0]] for value in count_populary],columns=["Characteristic","Yes","No"])
df_populary = pd.DataFrame([df_populary['No'].values, df_populary['Yes'].values],columns=df_populary['Characteristic'])
df_populary["Yes/No"]=["No","Yes"]

unpopulary= data[data['Pawpularity'] < 25]
count_unpopulary = {column:unpopulary[column].value_counts() for column in unpopulary.columns if not column == "Pawpularity" and not column == "Id"}
df_unpopulary = pd.DataFrame([[value,count_unpopulary[value][1],count_unpopulary[value][0]] for value in count_unpopulary],columns=["Characteristic","Yes","No"])
df_unpopulary = pd.DataFrame([df_unpopulary['No'].values, df_unpopulary['Yes'].values],columns=df_unpopulary['Characteristic'])
df_unpopulary["Yes/No"]=["No","Yes"]

# print(df_populary)

# print(data[(data['Subject Focus']==1) & (data['Pawpularity'] > 50)] )
# print(data[data["Pawpularity"] < 25])
# print(data[data["Pawpularity"] > 75])
# print(data['Pawpularity'].value_counts())

