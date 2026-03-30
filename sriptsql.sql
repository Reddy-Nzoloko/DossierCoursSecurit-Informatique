create DATABASE SecuriteInformatique;
use SecuriteInformatique;
CREATE TABLE utilisateur (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255) NOT NULL,
    postNom VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- selection des tous les utilisateurs
SELECT * FROM utilisateur;