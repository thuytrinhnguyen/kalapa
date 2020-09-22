def check_nas(df, column):
    count_nas = df[column].isna().sum()
    percentage_nas = count_nas / 30000
    return count_nas, percentage_nas

def unique_values(df, column):
    count_unique_values = df[column].value_counts()
    percentage_unique_values = count_unique_values / (df.shape[0] - df[column].isna().sum())
    return count_unique_values, percentage_unique_values
    
def values_only_in_set(df1, df2, column):
    values_only_in_df1 = set(df1[column].unique()) - set(df2[column].unique()) 
    return values_only_in_df1, len(values_only_in_df1)
    
def replace_by_column(df, column, terms, new_value):
    for term in terms:
        selection = df[column].str.contains(pat=term)
        selection[selection.isna()] = False
        df.loc[selection, column] = new_value