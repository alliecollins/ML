# Question 1 

#Note: pandas and sodapy installed separately
#token for open data portal: oV1MGQtvcsHOg4TbUazvY5zsB
#secret token: qDYlG3C9XDxehp2DtG2C_wEvQdxJVx1iEZQA

import pandas as pd
from sodapy import Socrata

def get_data():
	client = Socrata("data.cityofchicago.org", None)
	results = client.get("6zsd-86xi", where="year=2017 OR year=2018", limit=100000)
	results_df = pd.DataFrame.from_records(results)
	return results_df


def go():
    '''
    Go function
    '''
    get_data()

if __name__ == "__main__":
    go()