
sqlCreatePersTable = """ CREATE TABLE IF NOT EXISTS PERS (
                              PERS_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                              PERS_SURNAME TEXT NOT NULL,
                              PERS_FIRSTNAME TEXT NOT NULL,
                              PERS_BIRTHDATE TEXT NOT NULL
                              ); """

sqlCreatePhoneTable = """ CREATE TABLE IF NOT EXISTS PHONE (
                              PHONE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                              PHONE_MODELL TEXT UNIQUE NOT NULL,
                              PHONE_REALESE TEXT NOT NULL,
                              PHONE_PRICE INTEGER
                              ); """
                              
sqlCreateLokoTable = """ CREATE TABLE IF NOT EXISTS LOKO (
                          LOKO_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          PERS_ID INTEGER NOT NULL,
                          LOKO_DATE TEXT NOT NULL,
                          LOKO_BRUTTO INTEGER NOT NULL,
                          FOREIGN KEY(PERS_ID) REFERENCES PERS(PERS_ID) 
                        ); """

sqlCreateLocationsTable = """ CREATE TABLE IF NOT EXISTS LOCATIONS (
                              LOCATIONS_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                              LOCATIONS_LAT TEXT NOT NULL,
                              LOCATIONS_LNG TEXT NOT NULL,
                              LOCATIONS_ALT INTEGER NOT NULL,
                              LOCATIONS_TIMESTAMP TEXT NOT NULL
                              ); """

sqlInsertIntoLocations = """ INSERT INTO LOCATIONS(LOCATIONS_LAT,LOCATIONS_LNG,LOCATIONS_ALT, LOCATIONS_TIMESTAMP)
                    VALUES
                      (?,?,?,?);
                """
sqlInsertIntoPhone = """ INSERT INTO PHONE(PHONE_MODELL,PHONE_REALESE,PHONE_PRICE)
                    VALUES
                      (?,?,?);
                """

sqlInsertIntoPers = """ INSERT INTO PERS(PERS_SURNAME,PERS_FIRSTNAME,PERS_BIRTHDATE)
                    VALUES
                      (?,?,?);
                """

sqlInsertIntoLoko = """ INSERT INTO LOKO(PERS_ID,LOKO_DATE,LOKO_BRUTTO)
                    VALUES
                      (?,?,?);
                """
sqlPhone = [
    ("Moto G200", "November 2021", 59767),
    ("Motorola Defy", "July 2021", 36000),
    ("Motorola Edge 20 Pro", "August 2021", 56300),
    ("Motorola Edge Plus", "April 2020", 110900),
    ("Moto G100", "March 2021", 0),
]

sqlLocations = [
    ("48°14'10.4\"N", "16°22'12.1\"E", 161, "2001-08-28T12:10:53Z"),
    ("48°14'10.7\"N", "16°22'12.1\"E", 165, "2001-08-28T12:11:53Z"),
    ("48°14'10.8\"N", "16°22'11.9\"E", 176, "2001-08-28T12:12:55Z"),
    ("48°14'10.8\"N", "16°22'11.8\"E", 140, "2001-08-28T12:13:57Z"),
    ("48°14'10.7\"N", "16°22'11.8\"E", 175, "2001-08-28T12:14:59Z"),
]

sqlPers = [
    ("Okolie", "Jana", "2001-08-28"),
    ("Luinovic", "Malica", "2002-04-28"),
    ("Bogensperger", "Rupert", "2001-09-23"),
    ("Musterman", "Max", "2001-01-01"),
    ("Bouchalla", "Sonda", "2001-12-28"),
]

sqlLoko = [
    (1, "2001-08-28", 21321),
    (2, "2001-08-28", 21321),
    (3, "2001-08-28", 21321),
    (4, "2001-08-28", 21321),
    (5, "2001-08-28", 21321),
]