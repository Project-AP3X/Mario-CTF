DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS flags;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE flags(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  flag TEXT UNIQUE NOT NULL
);

INSERT INTO user (username, password) VALUES ('mario', 'peach');

INSERT INTO flags (flag) VALUES ('net-sec{m@mA-M!a}'), ('net-sec{Pl@y-G@m3}'), ('net-sec{Pr0f-r3ub-1s-aw3s0m3}'), ('net-sec{st3n0-ch@mP}');
