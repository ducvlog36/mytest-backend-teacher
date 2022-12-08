from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+pymysql://admin:ledinhduc1@classdb.cqgiripoozmq.ap-northeast-1.rds.amazonaws.com/mydb"

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()