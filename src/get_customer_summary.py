import os

def get_customer_summary():
    input_path = os.path.join(os.path.dirname(__file__), '../data/weebly/in/customer_info.csv')
    output_path = os.path.join(os.path.dirname(__file__), '../data/weebly/out/customer_summary.csv')

    f_in = open(input_path)
    f_out = open(output_path, "a+")

    geography_dict = dict()

    for line in f_in.readlines():
        # Exclude head
        if line != "customerid,country":
            # Split by comma
            try:
                customerid, country = line.split(",")
            except:
                pass

            if country not in geography_dict:
                geography_dict[country] = 1
            else:
                geography_dict[country] += 1

    f_in.close()

    for country, count in geography_dict.items():
        f_out.write(str(country)+","+str(count)+"\n")

    f_out.close()
