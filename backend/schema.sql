DROP TABLE IF EXISTS posts;

CREATE TABLE entry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    status BOOLEAN
)
