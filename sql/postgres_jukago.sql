CREATE DATABASE db_jukago;

CREATE USER jukago WITH PASSWORD 'putyourpasswordhere';

ALTER ROLE jukago SET client_encoding To 'utf8';

ALTER ROLE jukago SET default_transaction_isolation TO 'read committed';

-- pas nécessaire

-- ALTER ROLE jukago SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE db_jukago TO jukago;
