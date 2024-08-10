--registered in last 30 days--
SELECT * FROM Users
WHERE CreatedDate >= DATEADD(day, -30, GETDATE());

--total users with specific domain--
SELECT COUNT(*) FROM Users
WHERE Email LIKE '@gmail.com';

--update email of specific userid--
UPDATE Users
SET Email = 'new@gmail.com'
WHERE UserId = 123; 