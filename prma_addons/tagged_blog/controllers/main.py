from odoo import http
from odoo.http import request, Response
import json

class BlogTagsController(http.Controller):

    @http.route('/blog/tags/json', type='http', auth="public", website=True, csrf=False)
    def blog_tags_json(self, **post):
        try:
            tags = request.env['blog.tag'].sudo().search_read(
                [],
                ['id', 'name'],
                order='name asc'
            )
            return Response(
                json.dumps(tags),
                content_type='application/json;charset=utf-8'
            )
        except Exception as e:
            return Response(
                json.dumps({'error': str(e), 'code': 500}),
                content_type='application/json;charset=utf-8',
                status=500
            )
