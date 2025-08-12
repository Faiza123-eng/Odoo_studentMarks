from odoo import models, fields

class StudentMarks(models.Model):
    _name = 'student.marks'
    _description = 'Student Marks Record'

    name = fields.Char(string='Student Name', required=True)
    roll_number = fields.Char(string='Roll Number', required=True)
    subject = fields.Char(string='Subject')
    marks = fields.Integer(string='Marks')
