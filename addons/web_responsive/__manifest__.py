{
    "name": "Web Responsive",
    "summary": "Responsive web client, community-supported",
    "version": "13.0.3.3.0",
    "category": "Website",
    'website': 'https://witechenterprise.com/',
    'category': 'Manufacturing/Manufacturing',
    'author':  "LasLabs, Tecnativa, " "Odoo Community Association (OCA)," "witechenterprise",
    'sequence': 16,
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web", "mail"],
    "development_status": "Production/Stable",
    "data": ["views/assets.xml",
     "views/res_users.xml", 
     "views/web.xml"
     ],
    "qweb": [
        "static/src/xml/apps.xml",
        "static/src/xml/form_view.xml",
        "static/src/xml/navbar.xml",
        "static/src/xml/document_viewer.xml",
        "static/src/xml/discuss.xml",
    ],
}
