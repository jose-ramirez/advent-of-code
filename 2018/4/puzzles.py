from datetime import datetime
from collections import defaultdict
import time

def getTimestamp(log_string):
    data = log_string.split(' ')
    date = f"{data[0].replace('[', '')} {data[1].replace(']', '')}"
    dt_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
    s = time.mktime(dt_obj.timetuple())*1000
    return s

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def in_any(i, range_list):
    return any([i in r for r in range_list])

def get_sleep_track(log_object):
    if log_object['logs']:
        l = [0] * 61
        periods = list(map(lambda s: int(s.split(' ')[1][-3:-1]), log_object['logs']))
        ranges = list(map(lambda e: range(e[0], e[1]), pairwise(periods)))
        for i in range(61):
            l[i] = 1 if in_any(i, ranges) else 0
        return [log_object['start'].split(' ')[3][1:], l]
    else:
        return [log_object['start'].split(' ')[3][1:], [0] * 61]

def get_sleepiest(sleep_tracks):
    _dict = defaultdict(lambda: None)
    for track in sleep_tracks:
        if _dict[track[0]] is None:
            _dict[track[0]] = sum(track[1])
        else:
            _dict[track[0]] += sum(track[1])
    max_id = ''
    max_count = -1
    for k, v in _dict.items():
        if v > max_count:
            max_id, max_count = k, v
    return max_id, max_count

def get_sleepiest_per_minute(sleep_tracks):
    _dict = defaultdict(lambda: None)
    for track in sleep_tracks:
        if _dict[track[0]] is None:
            _dict[track[0]] = [track[1]]
        else:
            _dict[track[0]].append(track[1])
    new_dict = {}
    for k, v in _dict.items():
        times = list(map(sum, zip(*v)))
        max_times = max(times)
        new_dict[k] = [times.index(max_times), max_times]
    return new_dict

def get_all_sleep_tracks():
    sorted_logs = []
    with open('input.txt', 'r') as file:
        unsorted_logs = file.readlines()
        strip_newline = lambda s: s.strip()
        sorted_logs = sorted(unsorted_logs, key=getTimestamp)
        current_log_obj = defaultdict(lambda: None)
        sleep_tracks = []
        for line in sorted_logs:
            if "Guard" in line:
                if len(current_log_obj.keys()) > 0:
                    sleep_tracks.append(get_sleep_track(current_log_obj))
                    current_log_obj = defaultdict(lambda: None)
                current_log_obj['start'] = line
            else:
                if current_log_obj['logs'] == None:
                    current_log_obj['logs'] = [line]
                else:
                    current_log_obj['logs'].append(line)
        return sleep_tracks

def p1():
    tracks = get_all_sleep_tracks()
    sleepiest_id, sleep_time = get_sleepiest(tracks)
    my_tracks = filter(lambda r: r[0] == sleepiest_id, tracks)
    a, rows = list(zip(*my_tracks))
    totals_per_minute = list(map(sum, zip(*rows)))
    return totals_per_minute.index(max(totals_per_minute)) * int(sleepiest_id)

print(p1())

def p2():
    tracks = get_all_sleep_tracks()
    per_min_stats = get_sleepiest_per_minute(tracks)
    max_id = ''
    max_count = [-1, -1]
    for k, v in per_min_stats.items():
        if v[1] > max_count[1]:
            max_id, max_count = k, v
    return int(max_id) * max_count[0]

print(p2())