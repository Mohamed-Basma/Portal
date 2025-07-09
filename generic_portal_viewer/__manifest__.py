{
    "name": "Generic Portal Viewer",
    "version": "1.1",
    "summary": "Dynamic portal viewer with admin-managed screen config",
    "author": "ChatGPT",
    "depends": ["base", "portal", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/portal_templates.xml",
        "views/portal_view_config_form.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}