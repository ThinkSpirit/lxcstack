#!/usr/bin/env python
from sqlalchemy import *
import sys
import getopt

def usage():
    doc = \
"""usage:%s [-h] [-f file]
-h|--help           print help message
-f|--file file      database file
"""%sys.argv[0]
    print doc

dbfile = "lxcstack.db"

try:
    opts,args = getopt.getopt(sys.argv[1:],"hf:",["help","file="])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt,arg in opts:
    if opt in ("-h","--help"):
        usage()
        sys.exit()
    elif opt in ("-f","--file"):
        dbfile = arg

dbfile = "sqlite:///%s" % dbfile

db = create_engine(dbfile)
db.echo = False
metadata = MetaData(db)

user = Table('user', metadata,
    Column('user_uuid', String(32) , primary_key = True),
    Column('email_address', String(60), nullable = False),
    Column('password', String(32), nullable = False))


project = Table('project',metadata,
    Column('project_uuid',String(32),primary_key = True),
    Column('name',String(60),nullable = False),
    Column('description',String(256),nullable = True), # Chinese may be needed
    Column('manager',String(32),nullable = False)
)

machine = Table('machine',metadata,
    Column('machind_uuid',String(32),primary_key = True),
    #maybe many things!!!!!!
)

user_project_ship = Table('u_p_ship',metadata,
    Column('user_uuid',String(32),nullable = False),
    Column('project_uuid',String(32),nullable = False)
)

machine_project_ship = Table('m_p_ship',metadata,
    Column('machine_uuid',String(32),nullable = False),
    Column('project_uuid',String(32),nullable = False)
)

metadata.create_all(db)
