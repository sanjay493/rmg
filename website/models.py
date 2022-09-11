from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    fname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    create_date = db.Column(db.DateTime(timezone=True), default=func.now())
    rakedetails = db.relationship('Rakedetails')
    pr_dly = db.relationship('Pr_dly')


class Rakedetails(db.Model):
    __tablename__ = 'rakedetails'
    __table_args__ = (
        db.UniqueConstraint('rpt_date', 'unit', 'cust',
                            'rake_no', name='unique_component_commit'),
    )
    id = db.Column(db.Integer, primary_key=True)
    rpt_date = db.Column(db.Date)
    unit = db.Column(db.String(3))
    cust = db.Column(db.String(3))
    rake_no = db.Column(db.String(10))
    wgs_type = db.Column(db.String(2))
    lump_wg = db.Column(db.Integer)
    fines_wg = db.Column(db.Integer)
    arrival_time = db.Column(db.DateTime(timezone=True))
    pl_time = db.Column(db.DateTime(timezone=True))
    comp_time = db.Column(db.DateTime(timezone=True))
    lump_qty = db.Column(db.Integer)
    fines_qty = db.Column(db.Integer)

    entry_time = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Pr_dly(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rpt_date = db.Column(db.Date)
    unit = db.Column(db.String(3))
    comm = db.Column(db.String(1))
    act_qty = db.Column(db.Integer)
    entry_time = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
