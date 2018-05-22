import pandas as pd
import numpy as np
import os

def get_customer_geo_dist(input_file):
    input_path = input_file
    output_path = os.path.join(os.path.dirname(__file__), '../data/weebly/out/customer_summary.csv')

    customer_df = pd.read_csv(input_path)

    # Group by country and sum
    geo_dist_df = customer_df.groupby(['country']) \
                             .sum() \
                             .rename(columns={0:"country",1:"count"})

    geo_dist_df.to_csv(output_path)
