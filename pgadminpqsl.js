python3 manage.py dbshell

#add row to databse
#insert in query  editor : 

INSERT INTO 
    users(first_name,last_name,email,service,telephone,appointment_date)
VALUES
    ('Pepaa','pig','went','to', 'get', 'more'),
    ('to','get','more', 'of', 'that', 'yum')
RETURNING *;

iotablog_db=# INSERT INTO
iotablog_db=# users (first_name, last_name, email, service, telephone, appointment_date)
iotablog_db-# VALUES
iotablog_db-# ('Pepaa','pig','went','to', 'get', 'more'),
iotablog_db-# ('to','get','more', 'of', 'that', 'yum')
iotablog_db-# RETURNING *;
