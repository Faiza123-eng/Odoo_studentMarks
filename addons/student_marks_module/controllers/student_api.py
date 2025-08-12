from odoo import http
from odoo.http import request
import json

class StudentMarksAPI(http.Controller):

    @http.route('/api/student_marks', type='json', auth='user')
    def get_all_students(self):
        students = request.env['student.marks'].sudo().search([])
        return [
            {
                'id': student.id,
                'name': student.name,
                'roll_number': student.roll_number,
                'subject': student.subject,
                'marks': student.marks
            } for student in students
        ]

    @http.route('/api/student_marks/create', type='json', auth='user')
    def create_student(self, **kwargs):
        data = request.jsonrequest
        student = request.env['student.marks'].sudo().create({
            'name': data.get('name'),
            'roll_number': data.get('roll_number'),
            'subject': data.get('subject'),
            'marks': data.get('marks'),
        })
        return {'id': student.id, 'status': 'created'}
