# Vet Management App Project

This is my first full CodeClan project, which I built five weeks into the course to utilise my course-work up to this point.

This app was to be used on the management side to allow the vets to create a database with animal information, add new animals to the database, edit existing information and view all current information in the database. 

I elected to make my app about Kaiju as... Kaiju are awesome.

-----------------------------------------------------------------------------

![alt text](https://static.wikia.nocookie.net/godzilla/images/3/33/Godzilla_2021.jpg/revision/latest?cb=20210314011302 "Godzilla")

-----------------------------------------------------------------------------

### Made using the following (languages and applications):

  *HTML*

  *Jinja*

  *CSS*

  *Python*

  *Flask*

  *PSQL*
  
  *VS Code*

  *Git & Github*

-----------------------------------------------------------------------------

### Project Brief

**Vet Management App**
 
 A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.

-----------------------------------------------------------------------------

### MVP

**The practice wants to be able to register / track animals. Important information for the vets to know is:**

  *Name*

  *Date Of Birth (use a VARCHAR initially)*
  
  *Type of animal*
  
  *Contact details for the owner*
  
  *Treatment notes*
  
  *Be able to assign animals to vets*

  *CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?*
  
-----------------------------------------------------------------------------

### To use this app, you must perform the following steps

**Clone this repo:**

 Use Git to create a git folder and clone the repo to there.

**Create the database:**

 Createdb kaiju_vets_database

**Create the database tables:**

 psql -d vet_db -f db/kaiju_vets_database.sql

**Populate the database (console.py is pre-set tp perform this action):**

 python3 console.py

**Run the app (please ensure you have uploaded flask beforehand):**

 Flask run

-----------------------------------------------------------------------------

*I hope you enjoy and remember, I am still very much learning!*
