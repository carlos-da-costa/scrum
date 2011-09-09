# coding: utf8
# tente algo como
@auth.requires_login()
def index(): 
    sprints = db(db.sprint).select()
    return dict(sprints=crud.select(db.sprint))

@auth.requires_login()   
def novo():
    form = crud.create(db.sprint)
    response.view = 'simple_form.html'
    return dict(form=form)

@auth.requires_login()   
def editar():
    form = crud.update(db.sprint,request.args(0))
    response.view = 'simple_form.html'
    return dict(form=form)
