
DROP VIEW latest_login;

CREATE VIEW latest_login AS
SELECT login_record.id, users.id, username, user_vx_id, MAX(login_time), comment AS latest_login
FROM users LEFT OUTER JOIN login_record ON users.id = login_record.user_id
GROUP BY users.id ORDER BY users.id;