from QuandlDataProvider import QuandlDataProvider
from Charting import Charting
import argparse

#Setup arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--identifiers', help='Use -i to specify instrument identifiers')
parser.add_argument('-s', '--start_date', default='1990-01-01', help='Use -s to specify time series start date')
parser.add_argument('-e', '--end_date', default='2016-01-01', help='Use -e to specify time series end date')
parser.add_argument('-rw', '--rolling_window', default=20, help='Use -rw to specify rolling window length')
args = vars(parser.parse_args())

#Check arguments
if args['identifiers'] is None:
    print("No identifiers passed, please retry with parameter -i")
    raise ValueError("No identifiers passed")
else:
    instruments = args['identifiers'].split(',')

start_date = args['start_date']
end_date = args['end_date']
rolling_window = int(args['rolling_window'])

print("---------------------------------------")
print("Instrument Charting Tool")
print("Simon Nicholls")
print("---------------------------------------")
print("")
print("Parameters:")
print("Instruments: " + str(instruments))
print("Start Date: " + start_date)
print("End Date: " + end_date)
print("")


#Get instrument data and plot instruments
QDP = QuandlDataProvider()
CP = Charting()
threads = []
for instrument in instruments:
    try:
        print("Obtaining data for instrument identifier: " + instrument)
        instrument_values = QDP.get_instrument_value(instrument, start_date, end_date, rolling_window)
        CP.plot_graph(instrument, instrument_values)
    except Exception as ex:
        print("Error getting data for instrument: " + instrument + "Error: " + str(ex))


#Show all plots
print("Showing all plots, exit all to quit script")
CP.show_plots()


