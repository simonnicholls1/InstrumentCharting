from datetime import datetime
import pandas as pd
import nasdaqdatalink

class QuandlDataProvider:

    def get_instrument_value(self, symbol, start_date, end_date, rolling_window):

        nasdaqdatalink.ApiConfig.api_key = 'sVbiMBvfmdv8JxV417JK'
        # Get prices for symbol
        start_date_input = datetime.strptime(start_date,'%Y-%m-%d')
        end_date_input = datetime.strptime(end_date,'%Y-%m-%d')
        inst_data = nasdaqdatalink.get('FRED/' + symbol, start_date=start_date_input
                               ,end_date=end_date_input )

        # Convert to data frame and add median and mean
        inst_data_frame = pd.DataFrame({'value': inst_data['Value']}, index=inst_data.index)

        # Convert to data frame and add median and mean
        inst_data_frame = pd.DataFrame(
            {'value': inst_data['Value'],
             'rolling_mean': inst_data['Value'].rolling(center=False, window=rolling_window).mean(),
             'rolling_median': inst_data['Value'].rolling(center=False, window=rolling_window).median()},
            index=inst_data.index)

        inst_monthly_data_frame = inst_data_frame['value'].copy()
        inst_monthly_data_frame = \
            inst_monthly_data_frame.groupby(
                pd.PeriodIndex(inst_monthly_data_frame.index, freq="M")).mean().reset_index()


        #Remove NAs
        inst_data_frame = inst_data_frame.dropna()
        inst_monthly_data_frame = inst_monthly_data_frame.dropna()

        return inst_data_frame, inst_monthly_data_frame


if __name__== "__main__":
    #Test
    instrument_data = {}
    quandldp = QuandlDataProvider()
    data = quandldp.get_instrument_value('GDP', '1990-01-01', '2016-01-01', 20)
    print(data)


