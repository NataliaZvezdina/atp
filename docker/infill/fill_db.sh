#!/bin/bash
echo "Hello from ..hell"

DATABASE=$1
USERNAME=$2
HOSTNAME=$3

PGPASSWORD=$4 psql -h $HOSTNAME -U $USERNAME $DATABASE << EOF
insert into test(name,age) values('Bob',22), ('Alisa', 28) returning *;
select * from test
EOF