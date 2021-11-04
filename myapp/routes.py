from myapp import myapp_obj
from flask import render_template, flash, redirect
from myapp.forms import TopCities
from myapp import db
from myapp.models import City
db.create_all()

@myapp_obj.route("/", methods = ['GET', "POST"])
def main():
	form = TopCities()
	list = City.query.all()
	def myFunc(e):
		return e.rank
	list.sort(key = myFunc)
		
	if form.validate_on_submit():
		cityy = City(name = form.city_name.data, rank = form.city_rank.data, visited = form.is_visited.data)
		db.session.add(cityy)
		db.session.commit()
		flash(f'the city {form.city_name.data} has been added')
		return redirect("/")

	return render_template("Home.html", title = 'Top Cities!', top_cities = list, name = "Jason",  form=form)

