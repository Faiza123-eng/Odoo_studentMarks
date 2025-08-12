{
    'name': 'Student Marks',
    'version': '1.0',
    'summary': 'Manage student marks and API',
    'description': 'A simple module to manage student marks and expose API endpoints.',
    'author': 'Faiza',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_marks_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
