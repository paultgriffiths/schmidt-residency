
- Booleans as masks

- Dataframe merge
-- with methods left, right, inner outer
-- Distinct from join which is on indices

- Columns.str.contains('string_to_test_for')

-- Can be used to create mask

- Dropna and fillna

- df_sub['Estimated Number of Patients'].replace(0, float('nan')
Replace can use dictionary of keys(to find) and values to replace with

- groupby('City') then count number of entry in names column per city

-- groupby('city')["Name"].count()

if you want something fancier

- aggregate vs apply (vectorised?)
-- ind_total.agg(['sum', 'mean', np.std]) would give you sum, mean and standard devia
-- vs DF['col'].apply(fn_to_apply)

