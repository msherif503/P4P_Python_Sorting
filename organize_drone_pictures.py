import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime, timedelta
import shutil

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = {}
    if hasattr(image, '_getexif'):
        exif_info = image._getexif()
        if exif_info is not None:
            for tag, value in exif_info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
    return exif_data

def get_image_datetime(image_path):
    exif_data = get_exif_data(image_path)
    date_str = exif_data.get('DateTime', None)
    if date_str:
        return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    return None

def organize_pictures_by_date_and_flight(source_folder, dest_folder, time_threshold_minutes=10):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    picture_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]
    picture_files.sort()  # Ensure files are in order

    flights_by_date = {}

    for picture in picture_files:
        picture_path = os.path.join(source_folder, picture)
        picture_datetime = get_image_datetime(picture_path)

        if picture_datetime:
            date_str = picture_datetime.strftime('%Y-%m-%d')
            if date_str not in flights_by_date:
                flights_by_date[date_str] = []

            if not flights_by_date[date_str]:
                flights_by_date[date_str].append([picture_path])
            else:
                last_flight = flights_by_date[date_str][-1]
                last_picture_time = get_image_datetime(last_flight[-1])

                if (picture_datetime - last_picture_time) > timedelta(minutes=time_threshold_minutes):
                    flights_by_date[date_str].append([picture_path])
                else:
                    last_flight.append(picture_path)

    for date, flights in flights_by_date.items():
        date_folder_path = os.path.join(dest_folder, date)
        if not os.path.exists(date_folder_path):
            os.makedirs(date_folder_path)

        for i, flight in enumerate(flights):
            flight_folder_path = os.path.join(date_folder_path, f'Flight_{i+1:02d}')
            if not os.path.exists(flight_folder_path):
                os.makedirs(flight_folder_path)

            for picture_path in flight:
                shutil.move(picture_path, os.path.join(flight_folder_path, os.path.basename(picture_path)))

source_folder = 'C:\\Users\\moham\\DroneOrganizer\\source_folder'
dest_folder = 'C:\\Users\\moham\\DroneOrganizer\\dest_folder'
organize_pictures_by_date_and_flight(source_folder, dest_folder, time_threshold_minutes=1)
