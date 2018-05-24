import pandas as pd
import numpy as np
import os

def get_product_sells(invoice_file, product_file, product_sells_file):
    invoice_path = invoice_file
    product_path = product_file
    output_path = product_sells_file

    invoice_df = pd.read_csv(invoice_path, converters={'invoiceno': np.str_, \
                                                       'stockcode': np.str_, \
                                                       'quantity': np.int64, \
                                                       'invoicedate': np.str_, \
                                                       'customerid': np.str_})

    product_df = pd.read_csv(product_path, converters={'stockcode': np.str_, \
                                                       'description': np.str_, \
                                                       'unitprice': np.float64})

    invoice_full_info_df = pd.merge(invoice_df, product_df, on='stockcode', how='outer')

    product_sells_df = invoice_full_info_df.groupby('stockcode') \
                                           .aggregate({'quantity': lambda x: sum(x)}) \
                                           .rename(columns={'quantity': 'total_sells'}) \
                                           .sort_values('total_sells', ascending=False)


    product_sells_df.to_csv(output_path)
