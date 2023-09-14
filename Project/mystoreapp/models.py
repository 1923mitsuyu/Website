from . import db 

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(60), nullable=False, default = 'defaultcity.jpg')
    textbooks = db.relationship('Textbook', backref='Category', cascade="all, delete-orphan")

    def __repr__(self):
           # when this method gets called, it should print out the properties above 
           str = "Name: {}", "Description: {}", "Price: {}", "Image: {} \n" # {} = place holder 
           str = str.format(self.name, self.description, self.price, self.image)
           return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('textbook_id',db.Integer,db.ForeignKey('textbooks.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'textbook_id') )

class Textbook(db.Model):
    __tablename__ = 'textbooks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __repr__(self):
           # when this method gets called, it should print out the properties above 
           str = "ID: {}, Name: {}", "Description: {}","Price: {}", "Image: {}" , "Category_id:{}", "Date: {}\n" # {} = place holder 
           str = str.format(self.id, self.name, self.description, self.price, self.image, self.category_id, self.date)
           return str

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    textbooks = db.relationship("Textbook", secondary=orderdetails, backref="orders")

    def __repr__(self):
           # when this method gets called, it should print out the properties above 
           str = "ID: {}, Status: {}", "Date: {}", "Textbook: {}", "Total_cost: {}","Firstname: {}", "Surname: {}" , "Email:{}", "Phone: {}\n" # {} = place holder 
           str = str.format(self.id, self.status, self.date, self.textbook, self.total_cost, self.firstname, self.surname, self.email, self.phone)
           return str