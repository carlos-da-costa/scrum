# coding: utf8# tente algo como
@auth.requires(auth.has_membership(config.grupo_consultor) |
               auth.has_membership(config.grupo_desenvolvedor))
def index():    
    tickets = db((db.ticket.consultor == auth.user_id) |          (db.ticket.analista == auth.user_id)).select()
    return dict(tickets=SQLTABLE(tickets,headers='labels'))
   
@auth.requires(auth.has_membership(config.grupo_consultor))
def novo():
    response.view = 'simple_form.html'
    db.ticket.consultor.default = auth.user_id
    db.ticket.consultor.writable = False  
    form = crud.create(db.ticket)
    return dict(form=form)

@auth.requires(auth.has_membership(config.grupo_consultor) |
               auth.has_membership(config.grupo_desenvolvedor))
def editar():
    response.subtitle = 'Editar Ticket - %s ' % request.args(0) 
    form = crud.update(db.ticket,request.args(0),deletable=False)     
    imprimir = A(TAG.button('Imprimir'),_href=URL(r=request,c='ticket',f='imprimir',args=[request.args(0)]))  
    return dict(form=form,imprimir=imprimir)
   
def imprimir():
    response.view = 'ticket/form_teste.html'
    ticket = db(db.ticket.id == request.args(0)).select().first()
    return dict(ticket=ticket)
