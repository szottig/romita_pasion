# romita_pasion
Proyecto sobre una web de la Copa América 2024 desarrollado en python, Flask, SQLAlchemy y PostgreSQL

## Prerequisites

- Python 3.9 or later
- PostgreSQL
- Virtualenv (optional but recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dogonzalez-fiuba/romita_pasion.git
cd romita_pasion
```
### 2. Set Up Virtual Environment
Create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages.

```bash
pip install Flask Flask-SQLAlchemy psycopg2-binary

```

### 4. Configure PostgreSQL Database

a. Open PostgreSQL terminal.
```bash
psql postgres
```
b. Create a user and database.Sql

```bash
CREATE USER dorisgonzalezpernalete WITH ENCRYPTED PASSWORD 'romitapasion';
CREATE DATABASE copa_america;
GRANT ALL PRIVILEGES ON DATABASE copa_america TO dorisgonzalezpernalete;
```
c. Connect to the copa_america database.
```bash
psql -d copa_america
```
d. Create the tables.
```bash
-- Create teams table
CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    confederation VARCHAR(100) NOT NULL,
    badge_url VARCHAR(255)
);

-- Create players table
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    position VARCHAR(50),
    current_team VARCHAR(100),
    team_id INTEGER REFERENCES teams(id),
    photo_url VARCHAR(255)
);
```

e. Insert initial data. sql

```bash
-- Insert teams
INSERT INTO teams (name, confederation, badge_url) VALUES
('Argentina', 'CONMEBOL', 'https://a.espncdn.com/photo/2023/0417/r1160276_1000x1000_1-1.png'),
('Brazil', 'CONMEBOL', 'https://a.espncdn.com/photo/2022/0716/r1036946_1000x1000_1-1.png'),
('Chile', 'CONMEBOL', 'https://a.espncdn.com/photo/2022/0321/r989426_1024x1024_1-1.png'),
('Uruguay', 'CONMEBOL', 'https://a.espncdn.com/photo/2020/0213/r665662_595x595_1-1.png');

-- Insert players
INSERT INTO players (name, age, position, current_team, team_id, photo_url) VALUES
('Lionel Messi', 36, 'Forward', 'Inter Miami', 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqbCwnIYB5lP4cjn3SVHiEM_ookf207Nww6A&usqp=CAU'),
('Neymar Jr', 32, 'Forward', 'Al-Hilal', 2, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRibpz3vV3Tl4PNRQyIAkkHQhx-M8zieTGxhA&usqp=CAU'),
('Arturo Vidal', 37, 'Midfielder', 'Athletico Paranaense', 3, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDQF-0cy5oQn4MoFU-_p9OuA8RegPBIIWMjQ&usqp=CAU'),
('Luis Suárez', 37, 'Forward', 'Grêmio', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQumQbtigXYjxGz39q3YbQDtZAMky-RIGRUtVDMfHiQ2Ukd2wCDUztCqt02LhciccRJo3k&usqp=CAU');

```
###  5. Configure the Application
Update the config.py file with your database credentials.

python - flask
```bash
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://dorisgonzalezpernalete:romitapasion@localhost/copa_america'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
### 6. Run the Application

Make sure you are in the project root directory and your virtual environment is activated.

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```
Visit http://127.0.0.1:5000 in your browser to see the application running.


### Usage
```bash
Home Page: http://127.0.0.1:5000/
View Teams: http://127.0.0.1:5000/teams
Add Team: http://127.0.0.1:5000/teams/add
Edit Team: http://127.0.0.1:5000/teams/<id>/edit
Delete Team: http://127.0.0.1:5000/teams/<id>/delete
```

SQL Queries to Verify Data
a. Get all players with their photos:
```bash
SELECT name, age, position, current_team, photo_url FROM players;
```
b. Get all teams with their badges:
```bash
SELECT name, confederation, badge_url FROM teams;
```
### Contributing