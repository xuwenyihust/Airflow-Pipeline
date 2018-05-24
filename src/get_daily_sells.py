import pandas as pd
import numpy as np
import os

def get_daily_sells(invoice_file, product_file, daily_sells_file):
    invoice_path = invoice_file
    product_path = product_file
    output_path = daily_sells_file

    invoice_df = pd.read_csv(invoice_path, converters={'invoiceno': np.str_, \
                                                       'stockcode': np.str_, \
                                                       'quantity': np.int64, \
                                                       'invoicedate': np.str_, \
                                                       'customerid': np.str_})

    product_df = pd.read_csv(product_path, converters={'stockcode': np.str_, \
                                                       'description': np.str_, \
                                                       'unitprice': np.float64})

    invoice_unitprice_df = pd.merge(invoice_df, product_df, on=['stockcode'], how='outer')
    invoice_unitprice_df['total_price'] = invoice_unitprice_df['unitprice'] * invoice_unitprice_df['quantity']
    # Cut the invoicedate to only year-month-day
    invoice_unitprice_df['invoicedate'] = invoice_unitprice_df['invoicedate'].apply(lambda x: x.split()[0])

    daily_sells_df = invoice_unitprice_df.groupby('invoicedate') \
                                         .aggregate({'total_price': lambda x: sum(x)}) \
                                         .rename(columns={'total_price':"total_money"}) \
                                         .sort_values('total_money', ascending=False)

    daily_sells_df.to_csv(output_path)
