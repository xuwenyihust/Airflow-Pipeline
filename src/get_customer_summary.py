import os

def get_customer_summary():
    input_path = os.path.join(os.path.dirname(__file__), '../data/weebly/in/customer_info.csv')
    output_path = os.path.join(os.path.dirname(__file__), '../data/weebly/out/customer_summary.csv')

    f_in = open(input_path)
    f_out = open(output_path, "a+")

    customer_dict = dict()

    for line in f_in.readlines():
        # Exclude head
        if line != "customerid,country":
            # Split by comma
            try:
                customerid, country = line.split(",")
            except:
                pass

            if customerid not in customer_dict:
                customer_dict[customerid] = 1
            else:
                customer_dict[customerid] += 1

    f_in.close()

    for customerid, count in customer_dict.items():
        f_out.write(str(customerid)+","+str(count)+"\n")

    f_out.close()
