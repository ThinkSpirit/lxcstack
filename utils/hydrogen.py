#!/usr/bin/env python
from sqlalchemy import *
import sys
import getopt

def usage():
    doc = """usagesss"""
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

dbfile = "sqlite:///%s"%dbfile

db = create_engine(dbfile)
db.echo = False
metadata = MetaData(db)

user = Table('user', metadata,
    Column('user_id', Integer, primary_key = True),
    Column('user_name', String(16), nullable = False),
    Column('email_address', String(60), key='email'),
    Column('password', String(20), nullable = False))

metadata.create_all(db)
