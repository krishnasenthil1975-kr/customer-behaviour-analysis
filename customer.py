import pandas as pd
df=pd.read_csv('customerdetails.csv')
df.head()
info=df.info()
print(info)
dis=df.describe()
print(dis)
null=df.isnull()
print(null)
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))
##df.null().sum()
df.columns= df.columns.str.lower()
df.columns= df.columns.str.replace(' ','-')
col=df.columns
print(col)

#create a age group
labels=['young','adults','middle aged','adult']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
# create column purchase_frequency_days
frequency_mapping = {
'Fortnightly': 14,
'Weekly': 7,
'Monthly': 30,
'Quarterly': 90,
'Bi-Weekly': 14,
'Annually': 365,
'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
df[['purchase_frequency_days','frequency_of_purchases']].head(10)
df[['discount_applied','promo_code_used']].head(10)
df.columns

