use db;

CREATE TABLE IF NOT EXISTS users(
    UserID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    PRIMARY KEY (UserID)
);

INSERT INTO users(FirstName, Surname)
VALUES("Josua", "Kuenz"), ("Simon", "Fäs"), ("Levin", "Frankhauser"), ("Simon", "Amsler"), ("Seth", "Schmutz"), ("Leandro", "Aebi"), ("Lorenz", "Boss"), ("Tobias", "Topp"), ("Cem", "Akkaya");

CREATE TABLE IF NOT EXISTS calculatorHistory(
    ID int not null AUTO_INCREMENT,
    Result float NOT NULL,
    FirstNumber float NOT NULL,
    SecondNumber float NOT NULL,
    Operation varchar(10) NOT NULL,
    UserID int NOT NULL,
    PRIMARY KEY(ID),
    FOREIGN KEY (UserID) REFERENCES users(UserID)
);