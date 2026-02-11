import pandas as pd

# load the superstore sales csv file into a pandas dataframe
df = pd.read_csv('PercorsoFile')        

# inspect dataframe structure and data types
print(df.info())

# check and handle missing values
print(df.isnull().sum())

# standardize column names by converting them to lowercase and replacing spaces with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# remove duplicate rows if any
df.drop_duplicates(inplace=True)

# validate numeric columns (sales, profit, discount, quantity) for non-numeric values and handle them
numeric_cols = ['sales', 'profit', 'discount', 'quantity']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # convert to numeric, set non-convertible values to NaN
    df[col].fillna(0, inplace=True)  # replace NaN with 0   

# final check for duplicates after cleaning
df.drop_duplicates(inplace=True)

# clean date columns if necessary (e.g., convert to datetime format)
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')  # convert to datetime, set invalid dates to NaT
    df['order_date'].fillna(pd.Timestamp('1970-01-01'), inplace=True)  # replace NaT with a default date

#standardize categorical columns (e.g., region, category) by stripping whitespace and converting to lowercase
categorical_cols = ['region', 'category', 'sub_category', 'customer_name', 'product_name']
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.lower()  # remove leading/trailing whitespace and convert to lowercase


# create derived columns if useful, such as profit margin
df['profit_margin'] = df['profit'] / df['sales']
df['profit_margin'].fillna(0, inplace=True)  # handle division by zero  

#round profit margin to 2 decimal places
df['profit_margin'] = df['profit_margin'].round(2)

# final check for any remaining issues
print(df.info())

# save cleaned dataset to a new CSV file
df.to_csv('PercorsoFile', index=False)

# display all the datafame after cleaning
print(df)

