from get_calendar_events import get_events
from get_geocoordinates import get_lat_long
from get_address_from_latlng import get_address
from WallaceGrahamCode import getParkAndTime
from add_event import set_events
from walking_distance import get_walking_time
import datetime

if __name__ == '__main__':

    start_loc = ('37.80636','-122.43742')
    #event name, start time, (lat, long)
    weekly_events_list = get_events()

    for event in weekly_events_list:

        end_loc = event[2]
        startTime = event[1]

        # (parking complex) coords[0] = lat, coords[1] = long, total_estimated_time, probToParkOnStreet
        prk_lat_lng, drive_time, probStreetParking = getParkAndTime(start_loc, (str(end_loc[0]), str(end_loc[1])), startTime[:-9] + 'Z')
        parking_walk_time = get_walking_time(startTime, prk_lat_lng, end_loc)
        #
        start_time_obj = datetime.datetime.strptime(startTime, "%Y-%m-%dT%H:%M:%S%z")
        time_to_leave = start_time_obj - datetime.timedelta(hours=0, minutes = drive_time + parking_walk_time)
        end_of_drive = start_time_obj - datetime.timedelta(hours=0, minutes = parking_walk_time)

        # (event_name, location, start, end, prob_of_parking)
        set_events(event[0], start_loc, prk_lat_lng, time_to_leave.strftime("%Y-%m-%dT%H:%M:%S%z"), end_of_drive.strftime("%Y-%m-%dT%H:%M:%S%z"), probStreetParking)

