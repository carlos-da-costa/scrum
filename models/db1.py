#coding: utf8
BRAZILIAN_DATE = IS_DATE(format=T('%Y-%m-%d'), error_message=T('deve ser dd/mm/yyyy!'))

db.define_table('config',
                Field('grupo_desenvolvedor',db.auth_group),
                Field('grupo_consultor',db.auth_group),
                Field('grupo_administrador',db.auth_group))                           

#redirect(URL(r=request,c='config',f='index'))
#config = db(db.config).select().first()
#db.config.insert()
config = db(db.config).select()[0]

db.define_table('biv',
                Field('numero','integer'),
                Field('data','date',requires= BRAZILIAN_DATE),
                Field('versao'))
db.biv.id.represent = lambda id: A('Editar BIV %i' % db.biv[id].numero,_href=URL(r=request,f='edita_biv',args=[id]))                                                       

db.define_table('menu',
                Field('caminho'))
               
db.define_table('menu_dom',
                Field('codigo'),
                Field('descricao'),
                Field('nome'),
                Field('modulo'))
           
db.define_table('modulo',
                Field('codigo','integer'),
                Field('nome'))
               
db.define_table('sprint',
                Field('numero'),
                Field('inicio','date',requires=BRAZILIAN_DATE),
                Field('fim','date',requires=BRAZILIAN_DATE))
db.sprint.id.represent = lambda id: A('Editar %i' % id, _href=URL(r=request,c='sprint',f='editar',args=[id]))

db.define_table('estado_ticket',
                Field('nome'))
db.estado_ticket.id.represent = lambda id: A('Editar %i' % id,_href=URL(r=request,c='config',f='estado_ticket',args=[id]))

db.define_table('ticket',
                Field('chamado'),
                Field('sprint',db.sprint), 
                Field('consultor',db.auth_user),
                Field('analista',db.auth_user),
                Field('estado'),
                Field('patch','boolean'),
                Field('local_teste'))
db.ticket.analista.requires = IS_IN_DB(db((db.auth_user.id == db.auth_membership.user_id) & (db.auth_membership.group_id==config.grupo_desenvolvedor)),
                                       db.auth_user.id,'%(first_name)s',
                                       zero='Sem desenvolvedores')                                        
db.ticket.estado.requires = IS_IN_DB(db,db.estado_ticket.id,'%(nome)s')
db.ticket.sprint.requires = IS_IN_DB(db,db.sprint.id,'Sprint %(numero)s')
               
db.define_table('caso_teste',
                Field('ticket',db.ticket),
                Field('acao','text'),
                Field('resultado','text'),
                Field('anexo','upload'), 
                Field('ordem','integer'))

db.define_table('item_biv',
                Field('biv',db.biv),
                Field('ticket',db.ticket), 
                Field('menu','text',widget=SQLFORM.widgets.autocomplete(request,db.menu.caminho,limitby=(0,10), min_length=2)),
                Field('modulo',widget=SQLFORM.widgets.autocomplete(request,db.modulo.nome,limitby=(0,10), min_length=2)),
                Field('texto','text'))

db.define_table('teste',
                Field('ticket',db.ticket),
                Field('caso',db.caso_teste),
                Field('data','date'), 
                Field('resultado','text'),
                Field('conclusao'))      
              
config = db(db.config).select().first()

db.item_biv.id.represent = lambda id: SPAN(A('Editar',_href=URL(r=request,c='default',f='edita_biv',args=[db.item_biv[id].biv,id])))                
               
def insere_menu(form):       
    if len(form.vars.menu) > 0:
       db.menu.insert(caminho=form.vars.menu) 

def insere_modulo(form):
    if len(form.vars.modulo) > 0:
       db.modulo.insert(nome=form.vars.modulo)        
      
crud.settings.create_onaccept.item_biv.append(lambda form: insere_menu(form))
crud.settings.create_onaccept.item_biv.append(lambda form: insere_modulo(form))
