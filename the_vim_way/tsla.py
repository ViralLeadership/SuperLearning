import pandas_datareader as pdr
tsla = pdr.DataReader("tsla", data_source = "google",
        start = "2017-1-1")
tsla.head(8)
