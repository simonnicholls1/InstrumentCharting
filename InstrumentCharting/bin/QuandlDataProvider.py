from datetime import datetime
import pandas as pd
import quandl

class QuandlDataProvider:

    def get_instrument_value(self, symbol, start_date, end_date, rolling_window):

        quandl_key = 'sVbiMBvfmdv8JxV417JK'

        # Get prices for stock
        start_date_input = datetime.strptime(start_date,'%Y-%m-%d')
        end_date_input = datetime.strptime(end_date,'%Y-%m-%d')
        inst_data = quandl.get('FRED/' + symbol, start_date=start_date_input
                               , end_date=end_date_input, authtoken=quandl_key)

        # Convert to data frame and add median and mean
        inst_data_frame = pd.DataFrame({'value': inst_data['VALUE']}, index=inst_data.index)

        # Convert to data frame and add median and mean
        inst_data_frame = pd.DataFrame(
            {'value': inst_data['VALUE'], 'rolling_mean': inst_data['VALUE'].rolling(center=False, window=rolling_window).mean(),
             'rolling_median': inst_data['VALUE'].rolling(center=False, window=rolling_window).median()}, index=inst_data.index)

        #Remove NAs
        inst_data_frame = inst_data_frame.dropna()

        return inst_data_frame


if __name__== "__main__":
    #Test
    instrument_data = {}
    quandldp = QuandlDataProvider()
    data = quandldp.get_instrument_value('GDPMC1', '1990-01-01', '2016-01-01', 20)
    print(data)


