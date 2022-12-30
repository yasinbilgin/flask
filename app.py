from db_init import initialize

from flask import Flask, render_template, url_for, redirect, request, flash
from psycopg2 import extensions
from queries import *

extensions.register_type(extensions.UNICODE)
extensions.register_type(extensions.UNICODEARRAY)

app = Flask(__name__)
app.secret_key = "My Secret key"

os.environ['DATABASE_URL'] = "dbname='postgres' user='postgres' host='localhost' password='yasin123.'"
initialize(os.environ['DATABASE_URL'])


@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == "GET":
        tool_lists = select("id,name,brand", "tool_list", asDict=True)
        return render_template("home_page.html", tool_lists=tool_lists)
    elif request.method == "POST":
        insert_tool_list = (
            request.form['name'],
            request.form['brand']
        )
        insert("tool_list", "name,brand", insert_tool_list)
        flash("Tool Inserted Successfully")

        return redirect(url_for('home_page'))


@app.route("/update", methods=['GET', 'POST'])
def update_tool():
    if request.method == "POST":
        id_data = "id={}".format(request.form.get('id'))
        name = "name='{}'".format(request.form.get('name'))
        brand = "brand='{}'".format(request.form['brand'])

        update("tool_list", name, id_data)
        update("tool_list", brand, id_data)
        flash("Tool Updated Successfully")

        return redirect(url_for('home_page'))


@app.route("/delete/<id>/", methods=['GET', 'POST'])
def delete_tool(id):
    id_data = "id={}".format(id)

    delete("tool_list", id_data)
    flash("Tool Deleted Successfully")

    return redirect(url_for('home_page'))


if __name__ == "__main__":
    app.run(port="5000", debug=True)
