def compute_statistics(dataframe, column):

    mean = dataframe[column].mean()
    median = dataframe[column].median()
    std = dataframe[column].std()
    size = len(dataframe)
    
    return {'mean': mean, 'median': median, 'std': std, 'size': size}