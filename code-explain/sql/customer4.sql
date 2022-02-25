WITH alpha AS (
  SELECT NULL AS last_updated FROM users
  LIMIT 1
),
users AS (
  -- getting recently updated users
  UPDATE users SET password_hash = alpha.last_updated
  FROM alpha
  RETURNING name, address, purchase
)
SELECT name, address FROM users
WHERE purchase > 100.00
