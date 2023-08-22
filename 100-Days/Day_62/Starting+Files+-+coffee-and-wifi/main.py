from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def append_data_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message='Please fill out the field')])
    location = StringField('Cafe Location on Google Maps (URL)',
                           validators=[DataRequired(message='Please fill out the field'), URL(require_tld=True)])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired(message='Please fill out the field')])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired(message='Please fill out the field')])
    coffee = SelectField('Coffee Rating', validators=[DataRequired(message='Please select a field')],
                         choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                  ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'), ('✘', '✘')])
    wifi = SelectField('Wifi Strength Rating', validators=[DataRequired(message='Please select a field')],
                       choices=[('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'),
                                ('💪💪💪💪💪', '💪💪💪💪💪'), ('✘', '✘')])
    power = SelectField('Power Socket Availability', validators=[DataRequired(message='Please select a field')],
                        choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌️'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                 ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'), ('✘', '✘')])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee = form.coffee.data
        wifi = form.wifi.data
        power = form.power.data

        data = [cafe, location, open_time, close_time, coffee, wifi, power]

        append_data_to_csv(data, filename='cafe-data.csv')

        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        updated_row = list_of_rows[1:]

    return render_template('cafes.html', cafes=list_of_rows, updated_row=updated_row)


if __name__ == '__main__':
    app.run(debug=True)
