{
    'name': 'Product Kit Stages',
    'version': '1.0',
    'summary': 'Custom Kit with 4 Status Stages and Components Tab',
    'author': 'Bsma & ChatGPT',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/kit_component_views.xml',
        'views/kit_stages_views.xml',
    ],
    'installable': True,
    'application': True,
}
