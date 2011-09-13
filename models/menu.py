# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Carlos J. Costa'
response.meta.description = 'Development track'
response.meta.keywords = 'test, issue'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2007-2010'


##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('BIV'), False,'', [
                          (T('Novo'), False, URL('default','novo_biv'), []),
                          (T('Selecionar'), False, URL('default','selecionar_biv'), []),                    
                         ]),
    (T('Tickets'), False, URL('ticket','index'), [
                                                  (T('Novo'), False, URL('ticket','novo'), [] ),
                                                  (T('Selecionar'), False, URL('ticket','index'), [] )     
                                                 ]),
    (T('Sprint'), False, '', [
                              (T('Novo'), False, URL('sprint','novo'), [] ),
                              (T('Selecionar'), False, URL('sprint','index'), [] ) 
                             ]),
    (T('Config'), False, '', [
                              (T('Geral'), False, URL('config','index'), [] ),
                              (T('Estados de Tickets'), False, URL('config','estado_ticket'), [] ),
                              (T('Tipos de Ticket'), False, URL('config','tipo_ticket'), [] ), 
                              (T('Clientes'), False, URL('config','clientes'), [] ),
                              (T('Sistemas'), False, URL('config','sistemas'), [] ) 
                             ])                                                                 
    ]
