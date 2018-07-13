#!/usr/bin/env python

# Format the digitised Fort William pressure observations provided
#  by Ed Hawkins to match the images

from calendar import monthrange

# Load the observations from Ed's hPa file
import pandas
import numpy
ed_data=pandas.read_csv('../data/pressure_FW.csv',header=None)

# Hour from 1 to 24
def load_ob(year,month,day,hour):
    row=ed_data.loc[(ed_data.iloc[:,0]==year)  & 
                    (ed_data.iloc[:,1]==month) &
                    (ed_data.iloc[:,2]==day)]
    return row.values[0][hour+2]

def load_daily_average(year,month,day):
    row=ed_data.loc[(ed_data.iloc[:,0]==year)  & 
                    (ed_data.iloc[:,1]==month) &
                    (ed_data.iloc[:,2]==day)]
    return numpy.mean(row.values[0][3:27])

def load_by_hour_average(year,month,hour):
    row=ed_data.loc[(ed_data.iloc[:,0]==year)  & 
                    (ed_data.iloc[:,1]==month)]
    row=row.iloc[:,hour+2]
    return numpy.mean(row.values[0])

# Convert from hPa to inHg
def hpa2inhg(hpa):
    return hpa/33.8639

# Convert from inHg to print string
def toprt(inhg):
    inhg=inhg%10
    return "%05.3f" % inhg

# make CSV file with data for a month
def make_file(year,month):
    #
    file_name="../data/%04d-%02d.csv" % (year,month)
    #
    with open(file_name,'w') as opfile:
        header= '"Day",'
        for hour in range(1,25):
            header=header+"%2d," % hour
        header=header+'"Mean"'
        opfile.write(header+'\n')
        for day in range(1,monthrange(year,month)[1]+1):
            line='"%d",' % day
            for hour in range(1,25):
               hpa=load_ob(year,month,day,hour)
               line=line+"'"+toprt(hpa2inhg(hpa))+"'"+","
            # Add daily mean
            hpa=load_daily_average(year,month,day)
            line=line+"'"+toprt(hpa2inhg(hpa))+"'"+","
            opfile.write(line+'\n')
        # Add by-hour mean lines
        line='Mean,'
        for hour in range(1,26):  # hr25=>Use Ed's daily means
            hpa=load_by_hour_average(year,month,hour)
            line=line+"'"+toprt(hpa2inhg(hpa))+"'"+","
        opfile.write(line+'\n')

for year in range(1898,1905):
    for month in range(1,13):
        if year==1904 and month>9: continue
        make_file(year,month)
