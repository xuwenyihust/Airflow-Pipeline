import pandas as pd
import numpy as np
import os

def get_customer_geo_dist(input_file, output_file):
    input_path = input_file
    output_path = output_file

    customer_df = pd.read_csv(input_path)

    # Group by country and sum
    geo_dist_df = customer_df.groupby(['country']) \
                             .count() \
                             .rename(columns={'customerid':"count"})

    geo_dist_df.to_csv(output_path)
