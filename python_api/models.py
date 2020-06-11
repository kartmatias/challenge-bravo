from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence

Base = declarative_base()

class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer(unsigned=True, zerofill=True), 
                 Sequence('currency_id_seq', start=1, increment=1),   
                 primary_key=True)
    name = Column(String)
    code = Column(String)

    def __repr__(self):
        return "<Currency(name='%s', code='%s')" % (self.name, self.code)
class