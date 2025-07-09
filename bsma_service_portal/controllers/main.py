from odoo import http
from odoo.http import request

class PortalServiceRequest(http.Controller):

    @http.route('/my/service-requests', type='http', auth='user', website=True)
    def portal_service_requests(self, **kwargs):
        partner = request.env.user.partner_id
        requests = request.env['service.request'].sudo().search([('partner_id', '=', partner.id)])
        return request.render('bsma_service_portal.portal_service_requests_template', {
            'requests': requests
        })