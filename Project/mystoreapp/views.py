from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Textbook, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    textbooks = Textbook.query.order_by(Textbook.name).all()
    return render_template('index.html',textbooks=textbooks)

@main_bp.route('/textbook/<int:textbook_id>/')
def view_textbook(textbook_id):
    textbooks = Textbook.query.filter(Textbook.id == textbook_id)#.first()
    return render_template('product.html', textbooks=textbooks)

@main_bp.route('/category/<int:id>')
def view_category(id):
    category = Category.query.get(id)
    if category is not None:
        if id == 1:
            textbooks = Textbook.query.filter(Textbook.id.in_([5,6,7,8,9,10])).order_by(Textbook.name).all()
        elif id == 2:
            textbooks = Textbook.query.filter(Textbook.id.in_([1,2,3,11,12,18])).order_by(Textbook.name).all()
        elif id == 3:
            textbooks = Textbook.query.filter(Textbook.id.in_([4,13,14,15,16,17])).order_by(Textbook.name).all()
        else:
            textbooks = []
    
        return render_template('category.html', textbooks=textbooks, category=category)
    else:
        return render_template('category.html', textbooks=[], category=None)




# Referred to as "Basket" to the user
@main_bp.route('/order', methods=['POST','GET'])
def order():
    textbook_id = request.values.get('textbook_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None 

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for textbook in order.textbooks:
            totalprice = totalprice + textbook.price



 # are we adding an item?
    if textbook_id is not None and order is not None:
        textbook = Textbook.query.get(textbook_id)
        if textbook not in order.textbooks:
            try:
                order.textbooks.append(textbook)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    return render_template('order.html', order = order, totalprice=totalprice)

# Delete specific basket items
@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        textbook_to_delete = Textbook.query.get(id)
        try:
            order.textbooks.remove(textbook_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap basket
@main_bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for textbook in order.textbooks:
                totalcost = totalcost + textbook.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! One of our awesome team members will contact you soon...')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form)


@main_bp.route('/textbooks')
def search():

    search = request.args.get('search')

    search = '%{}%'.format(search) # substrings will match

    textbooks = Textbook.query.filter(Textbook.description.like(search)).all()

    return render_template('product.html', textbooks=textbooks)























