#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing pandas and importing the raw dataset of 2008.
import pandas as pd
df8 = pd.read_csv('all_alpha_08.csv')
df8.head()


# In[ ]:


#Some imformation about the dataset.
df8.info()


# In[ ]:


#Structure of the Dataset
df8.shape


# In[ ]:


#Number of duplicate rows in the Dataset
sum(df8.duplicated())


# In[ ]:


#Importing the second database of 2018
df18 = pd.read_csv('all_alpha_18.csv')
df18.head()


# In[ ]:


#structure of the database
df18.shape


# In[ ]:


#Some imformation about dataset 2018.
df18.info()


# In[ ]:


#Sum of duplicates in the dataset.
sum(df18.duplicated())


# In[ ]:


#unique values in SmartWay column in dataframe of 2008
df8['SmartWay'].unique()


# In[ ]:


#unique values in SmartWay column in dataframe of 2018
df18['SmartWay'].unique()


# In[ ]:


#unique values in Sales Area column in dataframe of 2008
df8['Sales Area'].unique()


# In[ ]:


#unique values in Cert region column in dataframe of 2008
df18['Cert Region'].unique()


# In[ ]:


#Number of unique values in Trans column in dataframe of 2008
len(df8['Trans'].unique())


# In[ ]:


#Number of unique values in Cyl column in dataframe of 2008
len(df8['Cyl'].unique())


# In[ ]:


#Number of unique values in Cyl column in dataframe of 2018
len(df18['Cyl'].unique())


# In[ ]:


#unique values in Fuel column in dataframe of 2018
df18['Fuel'].unique()


# In[ ]:


#unique values in Fuel column in dataframe of 2018
df8['Fuel'].unique()


# In[ ]:


#Deleting unwanted columns in dataframe 2008.
df8 = df8.drop(['Stnd','Underhood ID','FE Calc Appr','Unadj Cmb MPG'],axis=1)


# In[ ]:


df8


# In[ ]:


#Deleting unwanted columns in dataframe 2018.
df18 = df18.drop(['Stnd','Underhood ID','Stnd Description','Comb CO2'],axis=1)


# In[ ]:


df18


# In[ ]:


df8.shape


# In[ ]:


df18.shape


# In[ ]:


#Renaming The Sales Area as cert Region.
df8 = df8.rename({'Sales Area' : 'Cert Region'}, axis='columns')


# In[ ]:


df8.info()


# In[ ]:


#renaming every column in dataframe 2008 replacing " " by "_" and lower case every element.
df8.rename(columns=lambda x: x.strip().lower().replace(" ","_"),inplace=True)


# In[ ]:


df8.info()


# In[ ]:


#renaming every column in dataframe 2018 replacing " " by "_" and lower case every element.
df18.rename(columns=lambda x: x.strip().lower().replace(" ","_"),inplace=True)
df18.info()


# In[ ]:


#checking whether every column of each dataframe are of same name or not.
df8.columns == df18.columns


# In[ ]:


#saving both the datasets in CSV format.
df8.to_csv('dataset08.csv', index = False)
df18.to_csv('dataset18.csv', index = False)


# In[ ]:


#dealing with only datas where cert_region = CA
df8 = df8.query('cert_region == "CA"')


# In[ ]:


df18 = df18.query('cert_region == "CA"')


# In[ ]:


#checking if done correctly or not.
df8['cert_region'].unique()


# In[ ]:


df18['cert_region'].unique()


# In[ ]:


#dropping the cert region column as every datas are with same value = CA.
df18 = df18.drop(['cert_region'],axis=1)


# In[ ]:


df8 = df8.drop(['cert_region'],axis=1)


# In[ ]:


#checking whether the dataframers are with same column name or not.
df8.columns==df18.columns


# In[ ]:


df8.shape


# In[ ]:


#counting the number of null values in dataframe 2008.
df8.isnull().sum()


# In[ ]:


#counting the number of null values in dataframe 2018.
df18.isnull().sum()


# In[ ]:


#dropping the rows containing null values.
df8.dropna(inplace=True)
df18.dropna(inplace=True)


# In[ ]:


#again checking if there is any null values left.
df8.isnull().sum().any()


# In[ ]:


df18.isnull().sum().any()


# In[ ]:


#number of duplicate values.
print(df8.duplicated().sum())
print(df18.duplicated().sum())


# In[ ]:


#dropping the duplicates.
df8.drop_duplicates(inplace=True)
df18.drop_duplicates(inplace=True)


# In[ ]:


print(df8.duplicated().sum())
print(df18.duplicated().sum())


# In[ ]:


#saving the dataframe in CSV format.
df8.to_csv('dataset08.csv', index = False)
df18.to_csv('dataset18.csv', index = False)


# In[ ]:


df8.head()


# In[ ]:


df18.head()


# In[ ]:


df8.info()


# In[ ]:


df18.info()


# In[ ]:


#changing datatype from string to int.
df8['cyl'] = df8['cyl'].str.extract('(\d+)').astype(int)


# In[ ]:


df8.info()


# In[ ]:


#changing datatype from float to int.
df18['cyl'] = df18['cyl'].astype(int)


# In[ ]:


df18.info()


# In[ ]:


##changing datatype from string to float.
df8['air_pollution_score'] = df8['air_pollution_score'].str.extract('(\d+)').astype(float)


# In[ ]:


#changing datatype from int to float.
df18['air_pollution_score'] = df18['air_pollution_score'].astype(float)


# In[ ]:


#changing datatype from string to int.
df8['greenhouse_gas_score'] = df8['greenhouse_gas_score'].str.extract('(\d+)').astype(int)


# In[ ]:


df8.info()


# In[ ]:


#for each column changing datatype from string to float.
for column in ['city_mpg','hwy_mpg','cmb_mpg']:
    df8[column] = df8[column].str.extract('(\d+)').astype(float)
    df18[column] = df18[column].str.extract('(\d+)').astype(float)


# In[ ]:


df8.info()


# In[ ]:


df18.info()


# In[ ]:


#saving a copy to CSV.
df8.to_csv('dataset08.csv', index = False)
df18.to_csv('dataset18.csv', index = False)


# In[ ]:


df8


# In[ ]:


import pandas as pd
df8 = pd.read_csv('dataset08.csv')
df18 = pd.read_csv('dataset18.csv')


# In[ ]:


#some cars are with dual fuel operating system. For those cars we are creating different rows with fuels.
#creating dataframe with such models.
hb8 = df8[df8['fuel'].str.contains('/')]
hb8


# In[ ]:


hb18 = df18[df18['fuel'].str.contains('/')]
hb18


# In[ ]:


#copying one dataframe into two.
df1 = hb8.copy()
df2 = hb8.copy()


# In[ ]:


df1


# In[ ]:


#spliting and collecting the first values in dataframe 1.
df1['fuel'] = df1['fuel'].apply(lambda x: x.split("/")[0])


# In[ ]:


df1


# In[ ]:


#collecting the second values in dataframe 2.
df2['fuel'] = df2.fuel.str.split('/',expand=True)[1]


# In[ ]:


df2


# In[ ]:


#adding both the dataframes.
new_rows = df1.append(df2)
new_rows


# In[ ]:


#adding the new rows in the main dataframe.
df8.drop(hb8.index,inplace=True)
df8 = df8.append(new_rows, ignore_index=True)


# In[ ]:


#there is no more datas with "/".
df8[df8['fuel'].str.contains('/')]


# In[ ]:


df8.shape


# In[ ]:


#Repeating the steps in 2018 dataframe.
df1 = hb18.copy()
df2 = hb18.copy()


# In[ ]:


df1


# In[ ]:


df2


# In[ ]:


#spliting and collecting the first values in dataframe 1.
df1['fuel'] = df1['fuel'].apply(lambda x: x.split("/")[0])


# In[ ]:


#collecting the second values in dataframe 2.
df2['fuel'] = df2['fuel'].apply(lambda x: x.split("/")[1])


# In[ ]:


df1


# In[ ]:


df2


# In[ ]:


#adding both the dataframes.
new_rows = df1.append(df2)
new_rows


# In[ ]:


#adding the new rows in the main dataframe.
df18.drop(hb18.index,inplace=True)
df18 = df18.append(new_rows, ignore_index=True)


# In[ ]:


#there is no more datas with "/".
df18[df18['fuel'].str.contains('/')]


# In[ ]:


df18.info()


# In[ ]:


df18.info()


# In[ ]:


#checking the datatypes in dataframe 2008
df8.dtypes


# In[ ]:


#checking whether the datatypes are same in both dataframes.
df8.dtypes == df18.dtypes


# In[ ]:


#saving a copy.
df8.to_csv('dataset08.csv', index = False)
df18.to_csv('dataset18.csv', index = False)


# In[ ]:


#again importing the important libraries to create visualization.
import pandas as pd
import matplotlib.pyplot as plt
pd.get_option().run_line_magic('matplotlib', 'inline')
df8 = pd.read_csv('dataset08.csv')
df18 = pd.read_csv('dataset18.csv')


# In[ ]:


#histogramic plot
df8['greenhouse_gas_score'].hist()


# In[ ]:


#histogramic plot
df18['greenhouse_gas_score'].hist()


# In[ ]:


#histogramic plot
df8['cmb_mpg'].hist()


# In[ ]:


#histogramic plot
df18['cmb_mpg'].hist()


# In[ ]:


#plotting displacement against cmb_mpg
df8.plot('displ','cmb_mpg',figsize=(10,8))


# In[ ]:


#plotting greenhouse_gas_score against cmb_mpg
df8.plot('greenhouse_gas_score','cmb_mpg',figsize=(10,8))


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
pd.get_option().run_line_magic('matplotlib', 'inline')
df8 = pd.read_csv('dataset08.csv')
df18 = pd.read_csv('dataset18.csv')


# In[ ]:


#counting fuel wise values.
df8.fuel.value_counts()


# In[ ]:


df18.fuel.value_counts()


# In[ ]:


#creating dataframe for alternative fuel users.
alt_8 = df8.query('fuel in ["CNG", "ethanol"]').model.nunique()


# In[ ]:


alt_18 = df18.query('fuel in ["Electricity", "Ethanol"]').model.nunique()


# In[ ]:


#plotting number of unique models against alternative fuel.
plt.bar(["2008", "2018"], [alt_8, alt_18])
plt.title("Number of Unique Models Using Alternative Fuels",fontsize=15)
plt.xlabel("Year")
plt.ylabel("Number of Unique Models");


# In[ ]:


#getting total vaules in the dataframe.
total8 = df8.model.nunique()
total18 = df18.model.nunique()


# In[ ]:


#getting the proportion.
prop8 = alt_8 / total8
prop18 = alt_18 / total18


# In[ ]:


#plotting proportion of unique models against alternative fuel.
plt.bar(["2008", "2018"], [prop8, prop18])
plt.title("Proportion of Unique Models Using Alternative Fuels",fontsize=15)
plt.xlabel("Year")
plt.ylabel("Proportion of Unique Models");


# In[ ]:


#getting mean cmb__mpg by veh__class wise.
veh_08 = df8.groupby('veh_class').cmb_mpg.mean()
veh_08


# In[ ]:


veh_18 = df18.groupby('veh_class').cmb_mpg.mean()
veh_18


# In[ ]:


#increase in cmb_mpg veh_vlass wise.
inc = veh_18 - veh_08
inc


# In[ ]:


#plotting Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class.
inc.dropna(inplace=True)
plt.subplots(figsize=(8, 5))
plt.bar(inc.index, inc)
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG')


# In[ ]:


df8['smartway'].unique()


# In[ ]:


smart_8 = df8.query('smartway == "yes"')
smart_8.describe()


# In[ ]:


df18['smartway'].unique()


# In[ ]:


smart_18 = df18.query('smartway in ["Yes","Elite"]')
smart_18.describe()


# In[ ]:


#grater than mean of cmb_mpg.
top_08 = df8.query('cmb_mpg > cmb_mpg.mean()')
top_08.describe()


# In[ ]:


top_18 = df18.query('cmb_mpg > cmb_mpg.mean()')
top_18.describe()


# In[ ]:


#renaming columns of dataframe 2008 with '_2008' after first 10 characters.
df8.rename(columns=lambda x: x[:10] + "_2008", inplace=True)


# In[ ]:


df8.head()


# In[ ]:


#creating a left inner join for both dataframes.
df_combined = df8.merge(df18, left_on='model_2008', right_on='model', how='inner')
df_combined.head()


# In[ ]:


#saving the combined dataframe.
df_combined.to_csv('combined_dataset.csv', index=False)


# In[ ]:


#a new dataframe with cmb_mpg for both dataframes.
model_mpg = df_combined.groupby('model_2008')['cmb_mpg_2008','cmb_mpg'].mean()


# In[ ]:


model_mpg


# In[ ]:


# adding new column to show the increased value.
model_mpg['mpg_change'] =  model_mpg['cmb_mpg'] - model_mpg['cmb_mpg_2008']


# In[ ]:


model_mpg


# In[ ]:


#finding the maximum cmb_mpg increase.
max_mpg = max(model_mpg['mpg_change'])


# In[ ]:


# The model(s) with maximum cmb_mpg increase from 2008 to 2018.
model_mpg.query('mpg_change == {}'.format(max_mpg))


# In[ ]:




