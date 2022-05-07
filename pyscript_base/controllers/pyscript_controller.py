# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):

    @http.route('/pyscript/', auth='public', website=True)
    def pyscript_page(self, **kw):
        return http.request.render('pyscript_base.pyscript_template')
