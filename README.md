# **Table of Contents**

   * [Sells Module](#SellsModule)
   * [Usage](#usage)
   * [Description](#Description)
   * [DataBase Diagram](#DataBaseDiagram)


# Sells Module

- Vehicle purchase/sale manager.
- Control of payments and commissions.
- Node.js Frontend.
- Django Backend.
- PnP module (Plug-and-Play). 


# Description
> Project of higher degree of web application development. 

>We propose the simulation of a company that has contracted a freelance programmer to implement its website.

>This company needs to account for sales and payments made to suppliers and customers to conduct the company's business in the automotive trucking industry.

>In this web application, only the buyer, seller and users of the accounting department of the company will enter. Each user should have their own panel, and be able to see how their commercial agreements are being managed.

# Usage
- DataBase Steps (PSQL)
   - Create database
      - Command: CREATE DATABASE <name-of-database>;
   - Create user
      - Command: CREATE USER <name-of-user>;
   - Set password to user
      - Command: ALTER USER <name-of-user> WITH PASSWORD '<password>';
   - Grant privileges to database
      - Command: GRANT ALL PRIVILEGES ON DATABASE <name-of-database> TO <name-of-user>;

- Backend Steps
   - Turn on the virtual environment
   - Create the migrations
      - Command: python manage.py makemigrations
   - Apply the migrations to data base
      - Command: python manage.py migrate
   - Start Server
      - Command: python manage.py runserver

- Frontend Steps
   - Install Yarn with NPM
      - npm install yarn
   - Install modules to run proyect
      - Yarn install
   - Start server
      - Dev: Yarn dev
      - Prod: Yarn doit (custom command created in package.json)

# DataBase Diagram
### Legend
- Empty arrow = Inheritance
- Filled arrow = Relationship

![](https://github.com/CarlxsMG/proyectoClase/blob/main/BaseDeDatos.drawio.png)
