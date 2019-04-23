# Mobility
Mobility provide users data visualizations of the frequency of bikes and scooters in US's main regions.

## Table of Contents
* [Overview](#overview)</br>
* [Tech Stack](#techstack)</br>
* [Setup/Installation](#installation)</br>
* [Demo](#demo)</br>
* [Future Development](#future)</br>

<a name="overview"/></a>
## Overview

<a name="techstack"/></a>
## Tech Stack
**Frontend:** </br>
**Backend:** <br/>
**Libraries:** <br/>
**API:** <br/>

<a name="installation"/></a>
## Setup/Installation
On local machine, go to desired directory.  Clone protag repository:
```
$ git clone https://github.com/hacksnextdoor/mobility.git
```
Create a virtual environment in the directory:
```
$ virtualenv env
```
Activate virtual environment:
```
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Create database:
```
$ createdb music
```
Build database:
```
$ python3 -i model.py
>>> db.create_all()
```
Seed database:
```
$ python3 -i seed.py
```
Run app:
```
$ python3 server.py
```
Navigate to localhost:5000 in browser.

<a name="demo"/></a>
## Demo

**Enter a region.  Select desired result.**
<br/><br/>
![Homepage](/static/images/readme/homepage.gif)
<br/>

**Thanks for exploring!**

<a name="future"/></a>
## Future Development
* Enable region comparison.


