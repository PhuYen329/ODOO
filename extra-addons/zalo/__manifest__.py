# -*- coding: utf-8 -*-
{
    "name": "zalo",
    "summary": """Zalo Chat Model""",
    "description": """Managing Zalo Chat Information""",
    "author": "t4teck",
    "website": "https://www.mywebsite.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "zalo",
    "version": "0.1",
    "application": True,
    "auto_install": False,
    # any module necessary for this one to work correctly
    "depends": ["base", "product", "website", "account", "contacts", "mail"],
    # always loaded
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "views/zalo_menu_view.xml",
        "views/zalo_users.xml",
        "views/zalo_managers.xml",
        "view/zalo_contacts.xml",
        "views/zalo_settings.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
