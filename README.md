# Drone Picture Organizer


![P4P+(4)+copy-ed](https://github.com/msherif503/P4P_Python_Sorting/assets/69431662/de3c60fb-0f1e-4175-996d-ba7ec3c17eb8)

## Overview

The **Drone Picture Organizer** is a Python script designed to organize drone images by date and flight based on their EXIF metadata. This script sorts the pictures into folders by the day they were taken, and within each day's folder, it creates subfolders for each flight.

## Features

- **Automatic Organization**: Organizes pictures into date-based folders and flight subfolders.
- **EXIF Metadata Extraction**: Utilizes EXIF data to determine the date and time each picture was taken.
- **Customizable Time Threshold**: Allows customization of the time threshold to define separate flights.
- **User-Friendly**: Easy to set up and run with minimal configuration.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/YourUsername/DroneOrganizer.git
    cd DroneOrganizer
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare Folders**:
    - Create `source_folder` and `dest_folder` within the project directory.
    - Place your drone pictures in the `source_folder`.

2. **Run the Script**:
    ```bash
    python organize_drone_pictures.py
    ```

## Example Folder Structure


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


## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [DJI](https://www.dji.com/) for creating the Phantom 4 Pro drone.
- [Pillow](https://python-pillow.org/) for image processing capabilities.
