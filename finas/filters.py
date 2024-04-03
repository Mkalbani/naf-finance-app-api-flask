from finas import app

@app.add_template_filter
def get_level(level):
    if level == 1:
        level = 'Authorizing Officer'
    elif level == 2:
        level = 'Financial Officer'
    elif level == 3:
        level = 'Cashier'
    else:
        level = 'Clerk'
    return level