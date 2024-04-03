
'''
Marshmallow
--------------
'''

from finas.db import *

from flask_marshmallow import Marshmallow

from finas import app

ma = Marshmallow(app)

admn = ma.Nested("AdmnSchema")

# Sample Marshmallow Schemas, us this method to make yours

class AcctSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Acct
    include_fk = True

class AdmnSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = Admn
   include_fk = True #This includes foreignkeys

class BudcSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Budcont
    include_fk = True

class ComdsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comds
    include_fk = True

class LocsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Locs
    include_fk = True
        
class PersSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = Pers
   include_fk = True #This includes foreignkeys

class RanksSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ranks
    include_fk = True

class SubhSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subhead
    include_fk = True

class TranSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = Trans
   include_fk = True #This includes foreignkeys

class UnitsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Units
    include_fk = True