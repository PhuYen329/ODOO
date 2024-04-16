# -*- coding: utf-8 -*-
{
    "name": "Zalo",
    "summary": """Zalo Chat Model""",
    "description": """Managing Zalo Chat Information""",
    "author": "t4teck",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    "installable": True,
    "application": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "product", "website", "account", "contacts"],
    # always loaded
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        # "views/views.xml",
        # "views/templates.xml",
        "views/zalo_menu_view.xml",

    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
