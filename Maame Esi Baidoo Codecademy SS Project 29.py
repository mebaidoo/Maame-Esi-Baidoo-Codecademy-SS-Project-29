import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())
#Getting the frequencies of all countries in the manufacturer_country column and getting the 5th most frequent
print(car_eval["manufacturer_country"].value_counts().index[4])
#Calculating a table of proportions for countries
print(car_eval["manufacturer_country"].value_counts(normalize = True))
#Getting the different categories under buying_cost variable
print(car_eval["buying_cost"].unique())
#Converting the buying_cost column to type category since it is an ordinal categorical variable
buying_cost_categories = ["low", "med", "high", "vhigh"]
car_eval["buying_cost"] = pd.Categorical(car_eval.buying_cost, buying_cost_categories, ordered = True)
#Getting the median category of buying_cost after converting the categories to codes
median_category = buying_cost_categories[int(np.median(car_eval.buying_cost.cat.codes))]
print(median_category)
#Calculating a table of proportions for the luggage variable without the missing values
print(car_eval.luggage.value_counts(normalize = True))
#Calculating a table of proportions for the luggage variable and including the missing values in the calculation
print(car_eval.luggage.value_counts(normalize = True, dropna = False))
#There are no missing values as proportions are the same using dropna = False or dropna = True
#Calculating a table of proportions for the luggage variable using a different method
print(car_eval.luggage.value_counts() / len(car_eval.luggage))
#Getting the count and proportions of cars with five or more doors
print((car_eval.doors == "5more").sum())
print((car_eval.doors == "5more").mean())