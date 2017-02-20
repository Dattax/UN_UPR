# UN_UPR
This project is a project for CodeAlliance an Intiative of Benetech in development for the United Nations Universal Period Review

# Goals and completion

Below is a list of all accomplishments and tasks completed with this project.
* created a light-weight python web application that can be easily extended and will run on almost any hardware.
*Documented code to help further work.
* Converted templates so that they are faster to load. This was verified with Google webmaster tools.
* Created an environment that can use almost any sql engine, including PostGreSQL, MYSql, and SQLLite.

# Design Decisions

Our team made a few design decisions which we hope will help the project in the future. First, although we initially started working with django as that is what we were handed, there was not enough code to make it worth sticking with Django for an application of this type. We also wanted something that can be easily scalable (and indeed, I was able to serve 50000 requests a second from a Digital Ocean droplet that costed $5 a month). We also chose to cut down on the webpages in terms of what libraries they were loading, so that we could insure the website would load as fast as possible. In many instances and other countries, especially those developing countries, our research showed us that there are still people who are using Windows 98 and everything after that. This means that we need to use the bare minimum in new technologies. Similarly, we are going to be getting reviews from countries where internet access might not be what it is in the United States and other developing nations. The faster a page can load and the less bandwidth it can consume, the better for the consumers of this application. To this end, we chose to statically render and serve all pages with minimal javascript overhead.

#design structure

The design structure is as follows:
* requirements.txt: this is a list of all packages which we require to be installed.
* migrate.py: this script will create the initial structure of a database no matter which engine you are using. We currently default to a sqlite database for testing. If you make any changes to the model, be sure to run this.
* run.py: used to run the flask application in development mode. useful for testing.

##upr directory

* controlers: holds all endpoints and controlers.
* forms: Holds form logic. This is generally separate from the controlers due to the way flask handles forms.
* models: holds all models needed for individual objects.
* static: holds all static files, such as css, javascript and image files.
* templates: holds all static templates using Flask's native templating engine.
 * utils: holds all utility functions and scripts used globally on the site.


# To-do:

This project is mostly complete. We have a fully working login sysstem and registration. There is also a full user model created already.

## Login and Registration

* I forgot my password link
* remember me checkbox

##organization

* tie form to model.

##questions

All questions have been properly templated and are ready to go (see templates). The best solution for this would be to create a model that includes all questions and a tracking table. From there, you can keep track of which form or subsection the user is in or you can easily just check the database for the last field that is not null. While we previously were going to base this on decision trees, questions only generally rely on the question before it being complete, or in the case of a sub-section insuring that that subsection was chosen. This means that you need only look back at one question prior which can be done via the model.

# Installation

As noted before, we ran this on a digitalocean droplet and that performed perfectly. Initially we had planned to provide documentation on actual installation, but this link: [https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps](installing flask on Ubuntu) explains everything you will need to know. The only note-worthy point is to remember to use `pip install -r requirements.txt` to import all packages that are needed by the application itself.

## DEPENDENCIES

### Flask

[Flask](http://flask.pocoo.org/)

### Bootstrap

[Bootstrap](http://getbootstrap.com/) by Twitter. Licensed under [MIT](https://github.com/twbs/bootstrap/blob/master/LICENSE)

### Font Awesome Icons

[Font Awesome](http://fortawesome.github.io/Font-Awesome/) by Dave Gandy. Licensed under [MIT](http://opensource.org/licenses/mit-license.html)

### Data Providers

## Country Data
Extracted into country_data.json and taken from [peric.github.io/GetCountries](http://peric.github.io/GetCountries/) with source data provided by [geonames.org](http://www.geonames.org/).
TODO: call funcitons via their API. [Geonames.org API Docs](http://www.geonames.org/export/web-services.html)


