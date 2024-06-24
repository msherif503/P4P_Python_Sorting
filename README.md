Drone Picture Organizer
This project organizes drone pictures into folders by date and flight based on the timestamps in their EXIF metadata. Each day's pictures are placed in a separate folder, and within each date folder, there are subfolders for each separate flight.

Prerequisites
Python 3.x
Pillow library
Installation
Install Python 3.x:
Download and install Python from the official Python website. Make sure to check the box that says "Add Python to PATH" during installation.

Install Pillow:
Open Command Prompt and install the Pillow library by running:

bash
Copy code
pip install pillow
Usage
Prepare Folders:

Create a folder named DroneOrganizer in C:\Users\moham.
Inside DroneOrganizer, create two subfolders: source_folder and dest_folder.
Place all your drone pictures in source_folder.
Save the Script:

Save the provided Python script as organize_drone_pictures.py in C:\Users\moham\DroneOrganizer.
Run the Script:

Open Command Prompt.
Navigate to the DroneOrganizer directory:
bash
Copy code
cd C:\Users\moham\DroneOrganizer
Run the script:
bash
Copy code
python organize_drone_pictures.py
Script Explanation
The script performs the following steps:

Extract EXIF Data:

Extracts the EXIF metadata from each image to get the timestamp.
Organize Pictures by Date and Flight:

Sorts pictures by their timestamps.
Groups pictures into flights based on a time threshold (default is 1 minute). If the gap between consecutive pictures is greater than the threshold, it starts a new flight.
Create Directories and Move Pictures:

Creates folders for each date.
Within each date folder, creates subfolders for each flight.
Moves pictures into their respective flight folders.
Customization
You can customize the time threshold for determining a new flight by changing the time_threshold_minutes parameter in the script. The default is set to 1 minute.

Example Folder Structure
After running the script, the dest_folder will have the following structure:

yaml
Copy code
dest_folder
├── 2023-06-01
│   ├── Flight_01
│   ├── Flight_02
│   └── ...
├── 2023-06-02
│   ├── Flight_01
│   ├── Flight_02
│   └── ...
└── ...
License
This project is licensed under the MIT License.

Notes:
Adjust the source_folder and dest_folder paths as needed in the script.
Make sure all your drone pictures have proper EXIF metadata with timestamps.
This README provides a comprehensive guide for setting up and using the script, ensuring it is accessible to beginners.
