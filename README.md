# Mobility (README.md)
Mobility provides users with data visualizations of the frequency of bikes and scooters in US's main regions.  Mobility aggregates GBFS feeds to enable developers to build data visualizations.  Mobility allows developers to leverage the API in order to build client applications that show aggregated bike data.  Currently there are no services that incorporate all the feeds.  This project was inspired by implementing the [WoBike documentation](https://github.com/ubahnverleih/WoBike) into a single service.


![Imgur](https://i.imgur.com/ksTpEHQ.gifv)

## Table of Contents
- [Overview](https://github.com/Brandon05/mobility/blob/master/README.md#overview)
- [Tech Stack](https://github.com/Brandon05/mobility/blob/master/README.md#techstack)
- [Setup/Installation](https://github.com/Brandon05/mobility/blob/master/README.md#installation)
- [Demo](https://github.com/Brandon05/mobility/blob/master/README.md#demo)
- [Future Development](https://github.com/Brandon05/mobility/blob/master/README.md#future)
## Overview
## Tech Stack

**Frontend:** Using kepler.gl (React)

**Backend:** 

- Python 
- Flask

**Libraries:**

- Python
    - `flask`, `sqlalchemy`, and `requests`

**API:** 
**Get All Bikes by Region**

    # e.g. MIA, ATX for region
    $ curl "localhost:5000/<region>/all" 
    >> {
      "jumpbikes": {
          "data": {
            "bikes": [
              {
                "bike_id": "bike_96013", 
                "is_disabled": 0, 
                "is_reserved": 0, 
                "jump_ebike_battery_level": "49%", 
                "jump_vehicle_type": "scooter", 
                "lat": 25.794158, 
                "lon": -80.19069, 
                "name": "6211"
              }
              ...
            ]
          }
        }
      },
      "bird": {...}
    }
## Setup/Installation

**On local machine, go to desired directory. Clone** **mobility** **repository:**

    $ git clone https://github.com/hacksnextdoor/mobility.git

**Create a virtual environment in the directory:**

    $ virtualenv env

**Activate virtual environment:**

    $ source env/bin/activate

**Install dependencies:**

    $ pip install -r requirements.txt

**Run app:**

    $ FLASK_APP=mobility.py FLASK_DEBUG=1 flask run
    # Navigate to localhost:5000 in browser.
----------

**In Progress** 
**Create database:**

    $ createdb gbfs

**Build database:**

    $ python3 -i model.py
    >>> db.create_all()

**Seed database:**

    $ python3 -i seed.py
## Todo
- [ ] Integrate US clients
    - [x] Uber (Jump)
    - [ ] Lyft (Motivate) ;)
    - [ ] Bird
    - [ ] Lime
    - [ ] Spin
    - [ ] Scoot
- [ ] Setup DB 
    - [ ] Cache a days worth of data
- [ ] API
    - [ ] Grab bike by company `/<region>/<company>` e.g /mia/jumpbikes
    - [ ] Support time queries for endpoints `/<region>/all?since={epoch}&until={epoch}`
    - [ ] Filter by type `/<region>/all?type=scooter`
    - [ ] Filter by geohash `/<region>/all?geohash={hash}`
- [ ] Create Docker image
- [ ] Deploy to heroku or now with 1 click

