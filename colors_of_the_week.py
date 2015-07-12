# See: http://omz-forums.appspot.com/pythonista/post/5819625086386176

import calendar, ui

'''
    the colors corresponding to days of the week thai people often wear
    these colors on the day of the week. Is related to the Royal Family.
    Currently, the most important is yellow, the The King of Thailand
    was born on a Monday. He is the longest severing and living monach
    in the world.
'''

_day_color_dict = {day: color for day, color in zip(calendar.day_name,
                  'yellow pink green orange blue purple red'.split())}

for day in calendar.day_name:  # just for debugging
    print('{}: {}'.format(day, _day_color_dict[day]))

class MyTableViewDataSource (object):
    def tableview_cell_for_row(self, tableview, section, row):
        day = calendar.day_name[row]
        color = _day_color_dict[day]
        # 'subtitle'-style cells come with a built-in secondary label
        cell = ui.TableViewCell('subtitle')
        cell.background_color = 'black'
        cell.text_label.text = day
        cell.text_label.text_color = 'white'
        cell.detail_text_label.text = color
        cell.detail_text_label.text_color = color
        return cell

    def tableview_number_of_rows(self, tableview, section):
        return 7  # or len([x for x in calendar.day_name])

if __name__ == '__main__':
    tb = ui.TableView()
    tb.name='Colors of the Week'
    tb.background_color = 'black'
    tb.size_to_fit()
    tb.data_source = MyTableViewDataSource()
    tb.present('sheet')
