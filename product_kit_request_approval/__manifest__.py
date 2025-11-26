
{
    "name": "Product Kit Request with 3-Level Approval",
    "summary": "Create product with BoM (kit) after 3-level approval workflow",
    "version": "17.0.1.0.0",
    "category": "Inventory",
    "depends": ["product","mrp","mail"],
    "data": [
        "security/product_kit_request_groups.xml",
        "security/ir.model.access.csv",
        "data/product_kit_request_sequence.xml",
        "views/product_kit_request_views.xml"
    ]
}
