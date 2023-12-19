from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
def on_save(doc, method):
    if doc.stock_entry_type == "Material Transfer":
        StockEntry.on_submit(doc)