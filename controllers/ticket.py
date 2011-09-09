# coding: utf8# tente algo como
@auth.requires(auth.has_membership(config.grupo_consultor))
def index():    
    tickets = db((db.ticket.consultor == auth.user_id) | 
                 (db.ticket.analista == auth.user_id)).select()
    return dict(tickets=tickets)
   
@auth.requires(auth.has_membership(config.grupo_consultor))
def novo():
    response.view = 'simple_form.html'
    db.ticket.consultor.default = auth.user_id
    db.ticket.consultor.writable = False  
    form = crud.create(db.ticket)
    return dict(form=form)
