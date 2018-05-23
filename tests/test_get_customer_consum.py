import pandas as pd
import numpy as np
from src.get_customer_consum import get_customer_consum

# tmpdir fixture: per test temporary directory
def test_customer_consum(tmpdir):
    invoice_file = tmpdir.join('dummy_invoice.csv')
    product_file = tmpdir.join('dummy_product_info.csv')
    output_file = tmpdir.join('dummy_customer_consum.csv')

    invoice_file.write("invoiceno,stockcode,quantity,invoicedate,customerid\n537127,85123A,128,2010-12-05 12:13:00.000000,13831")

    product_file.write("stockcode,description,unitprice\n85123A,WHITE HANGING HEART T-LIGHT HOLDER,3.24")

    get_customer_consum(invoice_file.strpath, product_file.strpath, output_file.strpath)
    lines = output_file.readlines()

    assert lines[0] == "customerid,total_consum\n"
    assert lines[1] == "13831,414.72\n"
