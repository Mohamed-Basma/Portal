from odoo import http
from odoo.http import request

class GenericPortalViewer(http.Controller):

    @http.route('/my/custom-views', type='http', auth='user', website=True)
    def portal_custom_views(self, **kwargs):
        partner = request.env.user.partner_id
        configs = request.env['portal.view.config'].sudo().search([('active', '=', True)])
        return request.render('generic_portal_viewer.portal_view_config_list', {
            'configs': configs
        })

    @http.route('/my/custom-view/<int:config_id>', type='http', auth='user', website=True)
    def portal_model_list(self, config_id=None, **kwargs):
        config = request.env['portal.view.config'].sudo().browse(config_id)
        partner = request.env.user.partner_id
        Model = request.env[config.model_name].sudo()
        fields = [f for f in Model._fields if f not in ('id', '__last_update')]
        records = Model.search([('partner_id', '=', partner.id)])
        return request.render('generic_portal_viewer.template_model_list', {
            'records': records,
            'fields': fields,
            'model_name': config.model_name
        })

    @http.route('/my/custom-view/<model>/<int:record_id>', type='http', auth='user', website=True)
    def portal_model_detail(self, model=None, record_id=None, **kwargs):
        partner = request.env.user.partner_id
        Model = request.env[model].sudo()
        record = Model.browse(record_id)
        if record.partner_id.id != partner.id:
            return request.render('website.404')
        fields = [f for f in Model._fields if f not in ('id', '__last_update')]
        return request.render('generic_portal_viewer.template_model_detail', {
            'record': record,
            'fields': fields,
            'model_name': model
        })