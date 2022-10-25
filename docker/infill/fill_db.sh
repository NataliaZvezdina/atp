#!/bin/bash
echo "Hello from ..hell"

DATABASE=$1
USERNAME=$2
HOSTNAME=$3

PGPASSWORD=$4 psql -h $HOSTNAME -U $USERNAME $DATABASE << EOF
\copy test(name,age) from '/tmp/data.csv' with delimiter ',' csv header;
select * from test;
EOF