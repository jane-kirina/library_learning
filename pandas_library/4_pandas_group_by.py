import pandas as pd

dict_data = {
    'Product': ['BOOK', 'BOOK', 'GUITAR', 'GUITAR', 'CUP', 'CUP'],
    'Price': [30, 13, 20, 12, 23, 40]
}
df = pd.DataFrame(dict_data)
print(df)
data_product = df.groupby(['Product'])
print('Mean:')
print(data_product.mean())
print('Sum:')
print(data_product.sum())
print('Standard deviation:')
print(data_product.std())
