
CREATE TABLE IF NOT EXISTS vehicles (
    vin VARCHAR(17) PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    model_year INT NOT NULL,
    engine_type VARCHAR(50),
    country VARCHAR(50)
);
