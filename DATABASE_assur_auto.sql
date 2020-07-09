CREATE DATABASE IF NOT EXISTS assurauto;

CREATE TABLE IF NOT EXISTS clients(
	CL_ID INT NOT NULL PRIMARY KEY,
	CL_nom VARCHAR(15) NOT NULL,
    CL_prenom VARCHAR(30) NOT NULL,
	CL_adresse VARCHAR(50) NOT NULL,
    CL_codepostal VARCHAR(8) NOT NULL,
    CL_ville VARCHAR(20) NOT NULL CHECK('cannes'),
    CL_coordonnees VARCHAR(35) NOT NULL
);

CREATE TABLE IF NOT EXISTS contrat(
	CO_ID INT NOT NULL PRIMARY KEY,
    CO_nom VARCHAR(20) NOT NULL,
    CO_date DATE NOT NULL,
    CO_categorie VARCHAR(25) NOT NULL,
    CO_bonus_malus FLOAT NOT NULL,
    CL_clients_fk INT NOT NULL,
    FOREIGN KEY (CL_clients_fk) REFERENCES clients(CL_ID)
);

INSERT INTO clients (CL_ID, CL_nom, CL_prenom, CL_adresse, CL_codepostal, CL_ville, CL_coordonnees) VALUES 
(1, 'Dupont', 'Maurise', '20 rue de la poupee qui tousse', '06400', 'cannes','0645678972'),
(2, 'Martin', 'Phillipe', '309 route des informaticiens', '06400', 'cannes', '0673938490'),
(3, 'Durant', 'Bruce', '30 rue des elephants', '06400', 'cannes', '0634897129');

INSERT INTO contrat (CO_ID, CO_nom, CO_date, CO_categorie, CO_bonus_malus,CL_clients_fk) VALUES
(1, 'contrat auto', '2020/02/20', 'tout risque', 0.5, 1),
(2, 'contrat utilitaire', '2020/02/21', 'tiere', 2.3, 2),
(3, 'contrat auto', '2020/02/22', 'tout risque', 0.8, 3);
