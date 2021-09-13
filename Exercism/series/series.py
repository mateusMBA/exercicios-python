def slices(series, length):
    if (length > len(series) or length < 1 or series == ''):
        raise ValueError("Invalid parameters.")
    return [series[i:i+length] for i in range(0,len(series) - length +1)]
    
