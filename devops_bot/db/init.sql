CREATE USER repl_user WITH REPLICATION ENCRYPTED PASSWORD 'debian';
psql -U postgres -d db_tg;
CREATE TABLE Phones (
    phone VARCHAR(20) PRIMARY KEY
);
INSERT INTO Phones (phone) VALUES
    ('+79161234567'),
    ('+79269876543'),
    ('+79035671234'),
    ('+79548762345'),
    ('+79991234567');
