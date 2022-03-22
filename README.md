# Solar System API

## Goal

Our coding skills improve with repetition.

Our goal is to practice creating a minimal Flask API in a pair or group setting.

Pairing with other programmers will help create stronger understanding of the material, and improved skill at working with others. Software teams thrive on collaboration, so working side-by-side with someone while coding is vital!

In this activity, we will build a Solar System API. This API will store information about different planets.

We will focus on creating RESTful endpoints for CRUD operations.

## Tips

- Don't forget to work in a virtual environment
- Put endpoints in `app/routes.py`
- Add configuration, such as registering blueprints or configuring databases, in `app/__init__.py`
- Commit and push often

## Github Setup

1. Choose one member to fork the Solar System API repo 
1. Add all members to the forked repo as collaborators (through the repo settings)
1. All group members should clone this new, forked, group repo and `cd` into it
1. Discuss good git hygiene: 
    * Make regular commits
    * Push commits before switching driver
    * Pull before starting to drive

## Guidelines for Pair-Programming

- The driver is the person who is at the keyboard and mouse
- The navigator is the person who is thinking out loud, actively collaborating with the driver about the next step, and helping guide the development
- Trade-off driver and navigator roles often, at least daily, or every hour for longer work sessions.
- Take time to make sure you're on the same page

## Project Directions

### Part 1
1. [Wave 01: Read Endpoints](./project-directions/wave_01.md)


### Part 2
2. [Wave 02: Connecting the Database, Read and Create Endpoints](./project-directions/wave_02.md)
3. [Wave 03: Update and Delete](./project-directions/wave_03.md)
4. [Wave 04: Handling 404s](./project-directions/wave_04.md)
5. [Wave 05: Writing Tests](./project-directions/wave_05.md)

#### Database Setup/Update
For Waves 03, 04, and 05, the new driver may need to setup or update their database. Follow these steps:

1. Pull down all new git commits
1. Activate the virtual environment
1. Create the database `solar_system_development`
1. Run `flask db upgrade`
1. Run `flask run` to confirm that the API is running as expected
