import pandas as pd
import numpy as np
from get_customer_geo_dist import get_customer_geo_dist

# tmpdir fixture: per test temporary directory
def test_customer_geo_dist(tmpdir):
    input_file = tmpdir.join('dummy_customer_info.csv')
    output_file = tmpdir.join('dummy_customer_geo_dist.csv')

    input_file.write("customerid,country\n17519,United Kingdom\n17520,United Kingdom")

    get_customer_geo_dist(input_file.strpath, output_file.strpath)
    lines = output_file.readlines()
    assert lines[0] == "country,count\n"
    assert lines[1] == "United Kingdom,2\n"
