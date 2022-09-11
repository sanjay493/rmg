
import json
import os
from os import path
from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, send_from_directory, current_app, send_file
from .models import User, Rakedetails, Pr_dly
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from werkzeug.security import safe_join


class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully !', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.admin'))
            else:
                flash('Incorrecr password, try again !', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/admin')
@login_required
def admin():
    return render_template('admin.html', user=current_user)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 4 charecters. ', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 charecters. ', category='error')

        elif password != password1:
            flash('Password must be equal. ', category='error')

        elif len(password) < 6:
            flash('Password must be greater than 6 charecters. ', category='error')

        else:
            # add user to database
            new_user = User(email=email, fname=fname, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)

            flash('Account created !. ', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)


# @auth.route('/rakedetails', methods=['GET', 'POST'])
# @login_required
# def rakedetails():
    if request.method == 'POST':
        ldg_date = request.form.get('ldg_date')
        unit = request.form.get('unit')
        cust = request.form.get('cust')
        rake_no = request.form.get('rake_no')
        wgs_type = request.form.get('wgs_type')
        lump_wg = request.form.get('lump_wg')
        fines_wg = request.form.get('fines_wg')
        arrival_time = request.form.get('arrival_time')
        pl_time = request.form.get('pl_time')
        comp_time = request.form.get('comp_time')

        # add rakedetails entry to database
        new_rakedetails = Rakedetails(ldg_date=ldg_date, unit=unit, cust=cust, rake_no=rake_no, wgs_type=wgs_type, lump_wg=lump_wg,
                                      fines_wg=fines_wg, arrival_time=arrival_time, pl_time=pl_time, comp_time=comp_time, user_id=current_user.id)
        db.session.add(new_rakedetails)
        db.session.commit()

        flash('Rake entry submitted !. ', category='success')
        return render_template("rakedetails.html", user=current_user)
    return render_template("rakedetails.html", user=current_user)


@auth.route('/dly_production', methods=['GET', 'POST'])
@login_required
def dly_production():
    if request.method == 'POST':
        rpt_date = request.form.get('rpt_date')
        unit = request.form.get('unit')
        rm = request.form.get('rm')
        ob = request.form.get('ob')
        lump = request.form.get('lump')
        fines = request.form.get('fines')
        drill = request.form.get('drill')

        # add  entry to database
        lump_dly_production = Pr_dly(
            rpt_date=rpt_date, unit=unit, comm="L", act_qty=lump, user_id=current_user.id)
        fines_dly_production = Pr_dly(
            rpt_date=rpt_date, unit=unit, comm="F", act_qty=fines, user_id=current_user.id)
        rm_dly_production = Pr_dly(
            rpt_date=rpt_date, unit=unit, comm="RM", act_qty=rm, user_id=current_user.id)
        ob_dly_production = Pr_dly(
            rpt_date=rpt_date, unit=unit, comm="OB", act_qty=ob, user_id=current_user.id)
        drill_dly_production = Pr_dly(
            rpt_date=rpt_date, unit=unit, comm="DR", act_qty=drill, user_id=current_user.id)
        db.session.add(lump_dly_production)
        db.session.add(fines_dly_production)
        db.session.add(rm_dly_production)
        db.session.add(ob_dly_production)
        db.session.add(drill_dly_production)
        db.session.commit()

        flash('Report submitted !. ', category='success')
        return render_template("dly_production.html", user=current_user)
    return render_template("dly_production.html", user=current_user)


@auth.route('/rakedetails', methods=['GET', 'POST'])
@login_required
def rakedetails():
    if request.method == 'POST':
        rpt_date = request.form.get('rpt_date')
        unit = request.form.get('unit')
        cust = request.form.get('cust')
        rake_no = request.form.get('rake_no')
        wgs_type = request.form.get('wgs_type')

        lump_wg = request.form.get('lump_wg')
        fines_wg = request.form.get('fines_wg')
        arrival_time = request.form.get('arrival_time')
        pl_time = request.form.get('pl_time')
        comp_time = request.form.get('comp_time')

        lump_qty = request.form.get('lump_qty')
        fines_qty = request.form.get('fines_qty')

        # add rakedetails entry to database
        new_rakedetails = Rakedetails(
            rpt_date=rpt_date, unit=unit, cust=cust, rake_no=rake_no, wgs_type=wgs_type, lump_wg=lump_wg, fines_wg=fines_wg, arrival_time=arrival_time, pl_time=pl_time, comp_time=comp_time, lump_qty=lump_qty, fines_qty=fines_qty, user_id=current_user.id)

        db.session.add(new_rakedetails)

        db.session.commit()

        flash('Report submitted !. ', category='success')
        return render_template("rakedetails.html", user=current_user)
    return render_template("rakedetails.html", user=current_user)


# @auth.route('/upload_files/', methods=['GET', 'POST'])
# @login_required
# def upload_files():

#     if request.method == 'GET':
#         files = os.listdir(current_app.config['UPLOAD'])

#         return render_template("upload_files.html", user=current_user, files=files)

#     else:
#         uploaded_file = request.files['file']
#         filename = secure_filename(uploaded_file.filename)
#         if filename != '':

#             file_ext = os.path.splitext(filename)[1]
#             if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
#                 return "Invalid image", 400
#             uploaded_file.save(os.path.join(
#                 current_app.config['UPLOAD'], filename))

#             files = os.listdir(current_app.config['UPLOAD'])
#             return render_template("upload_files.html", user=current_user, files=files, file_ext=file_ext)

#         return '', 204


@ auth.errorhandler(413)
@ login_required
def too_large(e):
    return "File is too large", 413


# @auth.route("/download/<string:filename>")
# @login_required
# def download_files(filename):
#     try:
#         return send_from_directory(current_app.config["UPLOAD"], path=filename, as_attachment=True)
#     except FileNotFoundError:
#         abort(404)


@auth.route('/upload_files/', defaults={'req_path': ''})
@auth.route('/upload_files/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = current_app.config["UPLOAD"]

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files, user=current_user, req_path=req_path)
