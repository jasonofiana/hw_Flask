from myapp import db
class City(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(128), unique = True)
	rank = db.Column(db.Integer, index = True, unique = True)
	visited = db.Column(db.Boolean)
	def __repr__(self):
		return f'{self.name}'
