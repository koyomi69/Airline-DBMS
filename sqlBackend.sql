DROP DATABASE IF EXISTS airline;
CREATE DATABASE airline;
USE airline;

CREATE TABLE IF NOT EXISTS admin (
	User_ID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(45) NOT NULL,
    Password VARCHAR(45) NOT NULL,
    PRIMARY KEY(User_ID)
);

CREATE TABLE IF NOT EXISTS receptionist (
	Recep_ID INT NOT NULL AUTO_INCREMENT,
    Name VARCHAR(45) NOT NULL,
    Password VARCHAR(45) NOT NULL,
    PRIMARY KEY(Recep_ID)
);

CREATE TABLE IF NOT EXISTS passenger (
    CNIC BIGINT NOT NULL,
    Full_Name VARCHAR(45) NOT NULL,
    Phone BIGINT NOT NULL, 
    Address VARCHAR(200) NOT NULL,
    Nationality VARCHAR(45) NOT NULL,
    PRIMARY KEY(CNIC)
);

CREATE TABLE IF NOT EXISTS flight (
	Flight_ID VARCHAR(5) NOT NULL,
    Departure_Airport VARCHAR(3) NOT NULL,
    Arrival_Airport VARCHAR(3) NOT NULL,
    Departure TIME NOT NULL,
    Arrival TIME NOT NULL,
    Airplane VARCHAR(7) NOT NULL,
    Fare FLOAT NOT NULL,
    PRIMARY KEY(Flight_ID)
);

CREATE TABLE IF NOT EXISTS ticket (
	Ticket_Num INT NOT NULL AUTO_INCREMENT,
    CNIC BIGINT NOT NULL,
    Flight_ID VARCHAR(5) NOT NULL,
    PRIMARY KEY(Ticket_Num),
    FOREIGN KEY (CNIC) REFERENCES passenger(CNIC) ON DELETE CASCADE,
    FOREIGN KEY(Flight_ID) REFERENCES flight(Flight_ID) ON DELETE CASCADE
);

-- iNSERTING VALUES IN TABLE: ADMIN ->
INSERT INTO admin(Name, Password)
VALUES('Linda Goodman','TX435678');

INSERT INTO admin(Name, Password)
VALUES('Johnny Paul','638TXM');

INSERT INTO admin(Name, Password)
VALUES('James Pond','3321NEER');

INSERT INTO admin(Name, Password)
VALUES('Sherlock Momes','tophill');

INSERT INTO admin(Name, Password)
VALUES('Sheldon Cooper','345parkt');

INSERT INTO admin(Name, Password)
VALUES('RAJ Sharma','INDIA');

INSERT INTO admin(Name, Password)
VALUES('Nikita Gupta','SassyTx69');

INSERT INTO admin(Name, Password)
VALUES('Paul Gosh','port');

INSERT INTO admin(Name, Password)
VALUES('Pratik Courier','P2Cat');

INSERT INTO admin(Name, Password)
VALUES('Adit Gomes','654321');

-- iNSERTING VALUES IN TABLE: RECEPTIONIST ->
INSERT INTO receptionist(Name, Password)
VALUES('Laura Castle','1234');

INSERT INTO receptionist(Name, Password)
VALUES('Kim Possible','Kim123');

INSERT INTO receptionist(Name, Password)
VALUES('Donald Trump','DT6969');

INSERT INTO receptionist(Name, Password)
VALUES('Messi Boateng','zipper');

INSERT INTO receptionist(Name, Password)
VALUES('Ronaldo Boateng','dolars');

INSERT INTO receptionist(Name, Password)
VALUES('Katie Zelem','manchester');

INSERT INTO receptionist(Name, Password)
VALUES('Tim Arshard','red987');

INSERT INTO receptionist(Name, Password)
VALUES('Jimmy Turner','123456789');

INSERT INTO receptionist(Name, Password)
VALUES('Ayesha Sakki','jingle');

INSERT INTO receptionist(Name, Password)
VALUES('Usman Butt','lumssaxx');

-- iNSERTING VALUES IN TABLE: PASSENGER ->
INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410173009205,'Alen Smith',03210367290,'2230 NORTHSIDE, Albany','British');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410179876541,'Ankita Akir',03210367280,'3456 VIKAS APTS','Indian');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410172345698,'Suleiman Khan',03052267280,'7820 MCCALLUM COURTS','Pakistani');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410171002004,'Bob Dylan',03342367266,'7720 Dawood, DALLAS','American');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410179324666,'Mollie Green',03004360125,'9082 ESTAES OF RICHARDSON','Canadian');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410178765430,'Zoraiz Farooq',03006190505,'1110 FIR HILLS','Pakistani');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410179801235,'Sheikh Kamran',03004335126,'345 CHATHAM COURTS','Pakistani');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410171122334,'Akiyama Akiso',03050369290,'5589 PHASE 5 FHA','Japanese');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410171243567,'Mannan Haider',03217626643,'4444 FRANKFORD VILLA','Pakistani');

INSERT INTO passenger(CNIC,Full_Name,Phone,Address,Nationality)
VALUES(3410171243269,'Katie Zelem',03004568903,'7720 NEAT PUB','American');

-- iNSERTING VALUES IN TABLE: FLIGHT ->
INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('AI201','LHR','LND','02:10','08:15','ANJ-619',50500);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('QR230','KHI','BOM','19:20','21:05','ANJ-629',18200);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('EY123','LHR','KHI','10:20','11:55','ANJ-639',12500);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('LH987','LHR','NYK','18:10','04:55','ANJ-674',80620);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('BA168','KHI','TOR','20:00','23:50','ANJ-639',65050);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('AA436','ISL','LHR','02:15','03:55','AWJ-672',12200);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('QR190','LHR','KHI','13:00','14:55','AWJ-672',9400);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('BA305','ISL','TOK','18:50','20:40','AWJ-648',21320);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('EK345','KHI','ISL','23:00','1:45','AWJ-672',15220);

INSERT INTO flight(Flight_ID,Departure_Airport,Arrival_Airport,Departure,Arrival,Airplane,Fare)
VALUES('KW233','ISL','LHR','02:40','04:50','AWJ-672',11000);

-- iNSERTING VALUES IN TABLE: TICKET ->
INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410173009205,'AI201');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410179876541,'QR230');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410172345698,'EY123');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410171002004,'LH987');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410179324666,'BA168');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410178765430,'AA436');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410179801235,'QR190');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410171122334,'BA305');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410171243567,'EK345');

INSERT INTO ticket(CNIC,Flight_ID)
VALUES(3410171243269,'KW233');

