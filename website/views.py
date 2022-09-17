
from secrets import choice
from socket import IPPORT_RESERVED
from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User, Rakedetails, Pr_dly


import json
views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():

    query1 = "call dly_prod_eastn_grp()"
    query2 = "call dly_prod_analysis()"
    query4 = "call dly_prod_desp_bothgrp_analysis()"

    query7 = "call dly_plant_desp_cons_analysis()"
    query8 = "call periodic4_plant_desp_cons_analysis()"

    data = db.engine.execute(query1)
    data2 = db.engine.execute(query2)

    data4 = db.engine.execute(query4)

    data7 = db.engine.execute(query7)
    data8 = db.engine.execute(query8)
    labels = []
    values1 = []
    values2 = []
    values3 = []
    values4 = []

    # print(data)
    # print(query1)
    for data1 in data:
        labels.append(int(data1[1]))
        values1.append(int(data1[2]))
        values2.append(int(data1[3]))
        values3.append(int(data1[4]))
        values4.append(int(data1[5]))

    return render_template('home.html', user=current_user, max=80000, labels=labels, values1=values1, values2=values2, values3=values3, values4=values4, data2=data2,  data4=data4, data7=data7, data8=data8)


@views.route('/annual_Plant_Mines', methods=['GET'])
def annual_Plant_Mines():
    prod_ten = db.engine.execute("call last_ten_yrs_desp_prod()")
    return render_template("annual_Plant_Mines.html", prod_ten=prod_ten, user=current_user)


@views.route('/lump_recovery', methods=['GET'])
def lump_recovery():
    data = db.engine.execute("call last_ten_yrs_l_recovery();")
    myunits = []
    myFYs = []
    list = []

    for data1 in data:
        if data1.financial_year not in myFYs:
            myFYs.append(data1.financial_year)
        if data1.unit not in myunits:
            myunits.append(data1.unit)
        list.append(data1)
    return render_template("lump_recovery.html", user=current_user, myFYs=myFYs, myunits=myunits, lists=list)


@views.route('/mines_quality/', methods=['POST', 'GET'])
def mines_quality():
    if request.method == 'POST':
        unit = request.form['unit']
        cust = request.form['cust']
        periods = request.form['periods']
        data = []

        if not unit == 'Choose...' and not cust == 'Choose...' and not periods == 'Choose...':

            query2 = "call quality_annual_monthly_cust_unt('" + \
                periods+"','"+unit+"','"+cust+"')"

            # print(query2)

            data2 = db.engine.execute(query2)
            # print(data2)

            return render_template("mines_quality.html", user=current_user,  data2=data2, unit=unit, cust=cust, periods=periods)

    return render_template("mines_quality.html", user=current_user)


@views.route('/mines_data', methods=['POST', 'GET'])
def mines_data():
    if request.method == 'POST' and request.form['unit']:
        unit = request.form['unit']
        query = "call mines_annual_prod_rpt('"+unit+"')"
        data = db.engine.execute(query)
        print(query)
        return render_template("mines_data.html", data=data, user=current_user, unit=unit)
    return render_template("mines_data.html", user=current_user)


@views.route('/mines_monthly', methods=['POST', 'GET'])
def mines_monthly():
    if request.method == 'POST' and request.form['unit']:
        unit = request.form['unit']
        query = "call mines_monthly_prod_rpt('"+unit+"')"
        data = db.engine.execute(query)
        # print(data)
        return render_template("mines_monthly.html", data=data, user=current_user, unit=unit)
    return render_template("mines_monthly.html", user=current_user)


@views.route('/custom_mines_monthly', methods=['POST', 'GET'])
def custom_mines_monthly():
    if request.method == 'POST' and request.form['unit']:
        unit = request.form['unit']
        yymm1 = request.form['yymm1']
        yymm2 = request.form['yymm2']
        query = "call custom_mines_monthly_prod_rpt('" + \
            unit+"','"+yymm1+"','"+yymm2+"')"
        data = db.engine.execute(query)
        # print(data)
        return render_template("custom_mines_monthly.html", data=data, user=current_user, unit=unit)
    return render_template("custom_mines_monthly.html", user=current_user)


@views.route('/plant_data', methods=['POST', 'GET'])
def plant_data():
    if request.method == 'POST':
        cust = request.form['cust']
        query = "call plants_annual_prod_rpt('"+cust+"')"
        data = db.engine.execute(query)
        # print(data)
        return render_template("plant_data.html", data=data, user=current_user, cust=cust)
    return render_template("plant_data.html", user=current_user)


@views.route('/plant_monthly', methods=['POST', 'GET'])
def plant_monthly():
    if request.method == 'POST':
        cust = request.form['cust']
        query = "call plants_monthly_prod_rpt('"+cust+"')"
        data = db.engine.execute(query)
        # print(data)
        # print(query)
        return render_template("plant_monthly.html", data=data, user=current_user, cust=cust)
    return render_template("plant_monthly.html", user=current_user)


@views.context_processor
def context_processor():
    return dict(

    )


@views.route('/sail_links')
def sail_links():

    return render_template('sail_links.html', user=current_user)


@views.route('/graph')
def graph():
    query1 = "call ()"

    data = db.engine.execute(query1)
    return render_template('graph.html', user=current_user)


@views.route('/raketype_destwise', methods=['POST', 'GET'])
def raketype_destwise():
    if request.method == 'POST':
        cust = request.form['cust']
        query1 = "call `test`.rakes_type_destwise('"+cust+"')"

        data = db.engine.execute(query1)
        return render_template('raketype_destwise.html', user=current_user, data=data, cust=cust)
    return render_template('raketype_destwise.html', user=current_user)


@views.route('/rakes_mines_wise', methods=['POST', 'GET'])
def rakes_mines_wise():
    query1 = "call `test`.rakes_mines_wise()"
    data = db.engine.execute(query1)

    return render_template('rakes_mines_wise.html', user=current_user, data=data)


# @views.route('/dly_prodn', methods=['GET', 'POST'])
# def dly_prodn():
#     form = DlyProduction()
#     if form.validate_on_submit():
#         new_prodn = Dly_production(rpt_date=form.rpt_date.data,
#                                    unit=form.unit.data,

#                                    rm=form.rm.data,
#                                    ob=form.ob.data,
#                                    lump=form.lump.data,
#                                    fines=form.fines.data,
#                                    rm_trips=form.rm_trips.data,
#                                    ob_trips=form.ob_trips.data,
#                                    drill=form.drill.data,
#                                    user_id=current_user.id
#                                    )
#         lump_pr_dly = Pr_dly(rpt_date=form.rpt_date.data,
#                              unit=form.unit.data,
#                              comm="L",
#                              act_qty=form.lump.data,
#                              )
#         fines_pr_dly = Pr_dly(rpt_date=form.rpt_date.data,
#                               unit=form.unit.data,
#                               comm="F",
#                               act_qty=form.fines.data,
#                               )

#         db.session.add(new_prodn)
#         db.session.add(lump_pr_dly)
#         db.session.add(fines_pr_dly)

#         db.session.commit()

#         flash('Shift Report submitted !. ', category='success')
#         return redirect(url_for('views.dly_prodn', user=current_user))

#     return render_template('dly_prodn.html', form=form, user=current_user)


@views.route('/mthly_cust_wise_suppply', methods=['POST', 'GET'])
def mthly_cust_wise_suppply():
    if request.method == 'POST':
        unit = request.form['unit']
        yymm1 = request.form['yymm1']
        yymm2 = request.form['yymm2']
        comm1 = request.form['comm1']
        query = "call mthly_cust_wise_suppply('" + \
            unit+"','"+yymm1+"','"+yymm2+"','"+comm1+"')"
        data = db.engine.execute(query)
        # print(data)
        # print(query)
        return render_template("mthly_cust_wise_suppply.html", data=data, user=current_user, unit=unit)
    return render_template("mthly_cust_wise_suppply.html", user=current_user)


@views.route('/mthly_cust_mines_suppply', methods=['POST', 'GET'])
def mthly_cust_mines_suppply():
    if request.method == 'POST':
        cust = request.form['cust']
        yymm1 = request.form['yymm1']
        yymm2 = request.form['yymm2']
        comm1 = request.form['comm1']
        query = "call mthly_cust_mines_suppply('" + \
            cust+"','"+yymm1+"','"+yymm2+"','"+comm1+"')"
        data = db.engine.execute(query)
        # print(data)
        # print(query)
        return render_template("mthly_cust_mines_suppply.html", data=data, user=current_user, cust=cust)
    return render_template("mthly_cust_mines_suppply.html", user=current_user)


@views.route('/yrly_cust_wise_suppply', methods=['POST', 'GET'])
def yrly_cust_wise_suppply():
    if request.method == 'POST':
        unit = request.form['unit']
        comm1 = request.form['comm1']
        query = "call yrly_cust_wise_suppply('"+unit+"','"+comm1+"')"
        data = db.engine.execute(query)
        # print(data)
        # print(query)
        return render_template("yrly_cust_wise_suppply.html", data=data, user=current_user, unit=unit, comm=comm1)
    return render_template("yrly_cust_wise_suppply.html", user=current_user)


@views.route('/yrly_cust_mines_suppply', methods=['POST', 'GET'])
def yrly_cust_mines_suppply():
    if request.method == 'POST':
        cust = request.form['cust']
        comm1 = request.form['comm1']
        query = "call yrly_cust_mines_suppply('"+cust+"','"+comm1+"')"
        data = db.engine.execute(query)
        # print(data)
        # print(query)
        return render_template("yrly_cust_mines_suppply.html", data=data, user=current_user, cust=cust, comm=comm1)
    return render_template("yrly_cust_mines_suppply.html", user=current_user)


@views.route('/mines_performance', methods=['POST', 'GET'])
def mines_performance():
    if request.method == 'POST':

        yymm1 = request.form['yymm1']
        yymm2 = request.form['yymm2']
        comm1 = request.form['comm1']

        query = "call mines_performance('"+yymm1+"','"+yymm2+"','"+comm1+"')"
        data = db.engine.execute(query)
        # print(data)
        # print(query)
        return render_template("mines_performance.html", data=data, user=current_user, yymm1=yymm1, yymm2=yymm2, comm1=comm1)
    return render_template("mines_performance.html", user=current_user)
