- A percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations in a group of observations falls. For example, the 20th percentile is the value (or score) below which 20% of the observations may be found.

- Explicitly requesting a specific single row or column will return a pandas Series rather than a DataFrame 

- Use .loc[] for label-based indexing
		- If the row index was text-based (for example, passenger names), we can use .loc
		- Passing a single string returns a series; passing a list of columns to loc returns a dataframe
		- loc is more robust for looking up data, in that changes to the order or presence of rows or columns will not result in the wrong data being returned

- df.drop - axis =0 is drop based on row names, axis=1 is drop based on column names

- Can use inplace to save memory?  df.drop(['fare_category'], axis=1, inplace=True)

- values_count.to_dict = convert results to dictionary, values + counts

- df.set_index(column, drop=False) will prevent column being removed

- df.reset_index(inplace=True), reverts index to previous value [how?]

- Defning function to apply to column in dataframe row by row
``` def cat_fare(fare):
	    if fare < 50:
	        return 'cheap'
	    elif fare > 50:
	        return 'expensive'
	    else:
	        return None
```
 
- fare_cat=df['fare'].apply(cat_fare)

- Lambda to check if entry in Yes or yes

```
lambda: return entry if entry in ['yes','Yes'] else False 
```
