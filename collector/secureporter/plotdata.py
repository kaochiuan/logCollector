from json import JSONEncoder
import json
from datetime import timedelta
import datetime

class PlotData(object):
    """
    plot data struct for wq/chart.js
    id: series identifier
    label: label shown on chart
    unit: unit of series data
    itemlist: list of PlotItem object
    """
    def __init__(self, id=None, label=None, unit=None, itemlist=None):
        self.id = id
        self.label = label
        self.units = unit
        if itemlist is None:
            self.list = []
        else:
            self.list = itemlist

class PlotDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return obj.__dict__

class PlotItem(object):
    """
    plot data item to draw on chart
    the time-serial data is parid with date and value
    """
    def __init__(self, date=None, value=None):
        self.date = date
        if value is None:
            self.value = 0.0
        else:
            self.value = value

class PlotItemEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
            #return time.mktime(obj.timetuple()) * 1000
        else:
            return obj.__dict__

def main():
    datalst = []
    datalst.append(PlotItem(datetime.datetime.now(), 5.11))
    datalst.append(PlotItem(date=datetime.datetime.now()+timedelta(minutes=5), value=5.5))
    print(json.dumps(datalst, cls=PlotItemEncoder))

    plot = PlotData("1", "failrate", "%", datalst)
    print(json.dumps(plot, cls=PlotDataEncoder))

# if __name__ == "__main__":
#     main()








