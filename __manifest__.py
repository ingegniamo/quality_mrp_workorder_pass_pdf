# -*- coding: utf-8 -*-
{
    'name': "Quality mrp workorder pass pdf",
    
    'summary': "",
  
    'license': 'OPL-1',

    'author': "STeSI Consulting",

    'category': '',
  
    'version': '16.0.0.1',
  
    'website': "https://github.com/ingegniamo/quality_mrp_workorder_pass_pdf",

    # any module necessary for this one to work correctly
    'depends': ['quality_mrp_workorder','quality_control'],
    
    # always loaded
    'data': ['views/quality_views.xml'],

    'application': False,
}
