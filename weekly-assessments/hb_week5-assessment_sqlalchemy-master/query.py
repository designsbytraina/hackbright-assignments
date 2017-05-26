"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8. .get()

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.

Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter_by(founded=1903).filter(Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
    ## TRIED BOTH WAYS - THIS QUERY ISN'T WORKING:
    
    Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    query = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for name, brand_name, headquarters in query:
        print 'Name: %s, Brand: %s, Headquarters: %s' % (name, brand_name, headquarters)


def get_brands_summary():
    """Prints out each brand name, and each model name for that brand
     using only ONE database query."""

    ### Cannot get this to work, have tried group_by and order_by, 
    ### but the query mishandles brand_name after being run a few times.
        
    records = db.session.query(Model).order_by(Model.brand_name).all()

    #### Each record is formatted like so: 
        ### <Model id=15 year=1959 brand_name=Austin name=Mini>

    for record in records:
        print 'Make: %s, Model: %s' % (brand_name, name)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

    ### Value is <flask_sqlalchemy.BaseQuery object at 0x7ff4d78e9150>
    ### The datatype is a query object, meaning that you can obtain the records for this query by appending .all()

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

    ### An association table is like a middle table, in that it manages the relationship 
    ### between unrelated tables; it takes a foreign key from each table and creates a 
    ### many-to-many relationship between their records. While a middle table has meaningful
    ### values, an association table does not and only acts as the binding.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Function takes in a string as an argument and returns a list of brands
        whose name contains or is equal to that string."""
    
    ### Have tried multiple ways and not able to make string formatting work w/ SQLAlchemy.
    ### Are either of thse the right approach for handling substitutions?

    # query = Brand.query.filter(name.like(mystr + '%')).all()
    QUERY = """SELECT name
        FROM brands
        WHERE name LIKE :mystr
        """

    db_cursor = db.session.execute(QUERY, {'mystr':mystr}) #result proxy object

    return db_cursor.fetchall() #currently returning empty list, even when passing parameters


def get_models_between(start_year, end_year):
    """Function takes a start_year and end_year and returns a list of models
        whose year falls within that range."""

    query = db.session.query(Model).filter(Model.year.between(start_year, end_year))
    
    return query.all()


