# coding: utf-8

import datetime, json, requests, ui

auth = 'userid', 'passw0rd' # <-- API userid & password go here.
url = 'https://opendata.mycity.gov/get_current_BikeStationStatus_json'

map_url_fmt = 'http://maps.google.com/?q={location[lat]},{location[long]}'
station_dict = {'id': 1, 'location': {'lat': 43.608879, 'long': 3.8813495}}

def freshness(timestamp):
    def pluralize(label, count):  # 1 <label> or 2 <label>s
        return '{} {}{}'.format(count, label, '' if count == 1 else 's')
    timestamp = datetime.datetime.strptime(timestamp, '%Y%m%d%H%M%S')
    secs_old = int((datetime.datetime.now() - timestamp).total_seconds())
    mins_old = int(secs_old / 60)
    return pluralize(*('minute', mins_old) if mins_old else ('second', secs_old))

def do_api_get(url=url, auth=auth):  # caches results in a local file
    filename = url.partition('?')[0].rpartition('/')[2].split('_')[2] + '.json'  # BikeStationStatus.json
    data = requests.get(url, auth=auth, verify=False).json()
    if data:
        with open(filename, 'w') as out_file:
            json.dump(data, out_file)
        return data
    else:
        with open(filename) as in_file:
            return json.load(in_file)

def make_web_view_from_url(url):
    web_view = ui.WebView()
    web_view.load_url(url)
    w, h = ui.get_screen_size()
    web_view.frame = 0, 0, w, h
    return web_view

class BikeStationsView(ui.View):
    def __init__(self):
        #self.bikes_available = True
        self.seg_control = self.make_segmented_control(
            ('with available bikes', 'with no bikes available'))
        self.add_subview(self.seg_control)
        self.table_view = self.make_table_view()
        self.add_subview(self.table_view)
        ui.NavigationView(self).present()
        self.map_view = make_web_view_from_url(map_url_fmt.format(**station_dict))

    def make_segmented_control(self, segments):
        seg = ui.SegmentedControl()
        seg.action = self.layout
        seg.background_color = 'white'
        seg.flex = 'W'
        seg.height = 40
        seg.segments = segments
        seg.selected_index = 0
        seg.width = self.bounds.w
        return seg

    def make_table_view(self):
        x, y, w, h = self.bounds
        seg_height = self.subviews[0].height
        frame = x, y + seg_height, w, h - seg_height
        table_view = ui.TableView()
        table_view.data_source = ui.ListDataSource([])
        table_view.data_source.delete_enabled = False
        table_view.delegate = self
        table_view.flex = 'WH'
        table_view.frame = frame
        return table_view

    def layout(self, sender=None):
        ui.cancel_delays()
        if not self.navigation_view:
            return
        stations_dict = do_api_get(url, auth)
        self.navigation_view.name = 'Bike stations as of {} ago'.format(
            freshness(stations_dict['timeStamp']))
        stations = stations_dict['StationStatus']
        show_bikes_available = not self.seg_control.selected_index
        fmt = 'Station {id_} has {occ_} bikes available'
        self.table_view.data_source.items = [fmt.format(**x) for x
            in stations if bool(x['occ_']) == show_bikes_available]
        ui.delay(self.layout, 60)  # refresh at least once per minute

    def tableview_did_select(self, tableview, section, row):
        self.map_view.load_url(map_url_fmt.format(**station_dict))
        self.navigation_view.push_view(self.map_view)
        
BikeStationsView()
