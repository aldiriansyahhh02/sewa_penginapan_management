# Python CRUD Application for Rent accommodation management (Manajemen Sewa Penginapan)

A comprehensive Python application for managing Rent accommodation(Manajemen Sewa Penginapan) data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the hospitality industry, specifically addressing the need to manage Rent accommodation data efficiently. Rent accommodation Management plays a crucial role in CRUD information system to digitize all room data, price, bed type and room availability. With this system, accomodation owners and staff can monitor room occupancy status from the reception desk.

**Benefits:**

* Staff can directly input a new room and it's availability
* Staff can directly see the availability of the room and the price
* Staff can update the room data if there is some change 
* Staff can delete the room if it's not available anymore

**Target Users:**

This application is designed for hotel staff within the organization to facilitate their room management related to Rent Accomodation Management.

## Features

* **Create:**
    * Add new room entries with essential details like room-type, price, bed-type and room availability.
* **Read:**
    * Search and retrieve specific room records by applying filters based on room-type, bed-type and room availability.
    * Display comprehensive information for each room in a user-friendly format.
* **Update:**
    * Modify existing room data to reflect changes in room-type, price, bed-type and room availability.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of un-use rooms records with appropriate authorization checks.
* **Reporting:**
    * Generate reports or summaries based on room data to support hospitality industry.

## Installation

1. **Prerequisites:**
    * Python version 3.14.5

2. **Installation:**
    ```bash
    git clone https://github.com/aldiriansyahhh02/sewa_penginapan_management.git
    cd sewa_penginapan_management
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new room record with a detail based on room-type, price, bed-type and room availability.
    * **Read:** Search and retrieve room information by room-type, bed-type, or room availability.
    * **Update:** Modify room details, such as updating the whole room data.
    * **Delete:** Remove an un-used room if it's possible.

## Data Model
This project utilizes a [Data Structure] (e.g., relational database, JSON documents) to represent [Data Entity] data. The following fields are typically stored:
   * [data_kamar]: (List) - data_kamar serve as a database to store all existing room, allowing the data to be easily added, searched, modified or deleted.
   * [kamar_baru]: (Dictionary) - kamar_baru serve as an identification card that records the complete details of a specific room (ID, room-type, price, bed-type, and room availability), ensuring the data is neatly organized and kept distinct.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to m.aldiriansyahhh2@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

