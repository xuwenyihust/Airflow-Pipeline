import pandas as pd
import numpy as np
from src.get_daily_sells import get_daily_sells

# tmpdir fixture: per test temporary directory
def test_product_sells(tmpdir):
    invoice_file = tmpdir.join('dummy_invoice.csv')
    product_file = tmpdir.join('dummy_product_info.csv')
    output_file = tmpdir.join('dummy_daily_sells.csv')

    # Dummy data
    invoice_file.write("invoiceno,stockcode,quantity,invoicedate,customerid\n537127,85123A,128,2010-12-05 12:13:00.000000,13831")
    product_file.write("stockcode,description,unitprice\n85123A,WHITE HANGING HEART T-LIGHT HOLDER,3.24")

    get_daily_sells(invoice_file.strpath, product_file.strpath, output_file.strpath)
    lines = output_file.readlines()

    try:
        assert lines[0] == "invoicedate,total_money\n"
        assert lines[1] == "2010-12-05,414.72\n"
    except AssertionError as e:
        for i in range(len(lines)):
            print(lines[i])
        raise Exception(e.args)
