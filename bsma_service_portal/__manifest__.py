{
    "name": "Service Portal View",
    "version": "1.0",
    "summary": "Allow portal users to view their service requests",
    "author": "Your Name",
    "depends": ["base", "website", "portal"],
    "data": [
        "security/ir.model.access.csv",
        "security/record_rules.xml",
        "views/portal_templates.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}