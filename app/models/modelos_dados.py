# /app/models/modelos.py

from . import db

class Features(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Modelo de dados com três características
    feature_1 = db.Column(db.Float, nullable=False)
    feature_2 = db.Column(db.Float, nullable=False)
    feature_3 = db.Column(db.Float, nullable=False)

    # Relação com Labels
    label_id = db.Column(db.Integer, db.ForeignKey('labels.id'))
    label = db.relationship('Labels', backref='features')

    def __repr__(self):
        return f'<Features {self.id}: {self.feature_1}, {self.feature_2}, {self.feature_3}>'

class Labels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Labels {self.id}: {self.label}>'
