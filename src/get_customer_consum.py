import pandas as pd
import numpy as np
import os

def get_customer_consum(invoice_file, product_file, customer_consum_file):
    invoice_path = invoice_file
    product_path = product_file
    output_path = customer_consum_file

    invoice_df = pd.read_csv(invoice_path, converters={'invoiceno': np.str_, \
                                                       'stockcode': np.str_, \
                                                       'quantity': np.int64, \
                                                       'invoicedate': np.str_, \
                                                       'customerid': np.str_})
    product_df = pd.read_csv(product_path, converters={'stockcode': np.str_, \
                                                       'description': np.str_, \
                                                       'unitprice': np.float64})

    # Outer join invoice.csv & product_info.csv on column 'stockcode'
    invoice_unitprice_df = pd.merge(invoice_df, product_df, on=['stockcode'], how='outer')
    invoice_unitprice_df['total_price'] = invoice_unitprice_df['unitprice'] * invoice_unitprice_df['quantity']
    # Avoid index (0,1,2,3,...)
    # invoice_unitprice_df.to_csv(output_path, index=False)

    # Group by customerid and sum unitprice * quantity
    consum_amount_df = invoice_unitprice_df.groupby(['customerid']) \
                                    .aggregate({'total_price': lambda x: sum(x)}) \
                                    .rename(columns={'total_price':"total_money"}) \
                                    .sort_values('total_money', ascending=False)

    consum_count_df = invoice_unitprice_df.groupby(['customerid']) \
                                          .aggregate({'invoiceno': lambda x: x.nunique()}) \
                                          .rename(columns={'invoiceno': "total_times"})

    # consum_amount_df.to_csv(output_path, index=False)
    # consum_count_df.to_csv(output_path, index=False)
    customer_consum_df = pd.merge(consum_amount_df, consum_count_df, left_index=True, right_index=True, how='outer')
    customer_consum_df.to_csv(output_path)
