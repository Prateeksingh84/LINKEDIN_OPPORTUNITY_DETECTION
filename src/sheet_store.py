# src/sheet_store.py

def append_opportunity(sheet, opportunity):
    """
    Appends an opportunity to the provided sheet.

    Args:
        sheet (object): The sheet object to append data to.
        opportunity (dict): A dictionary containing opportunity details.
    """
    row = [
        opportunity["id"],
        opportunity["author_name"],
        opportunity["company"],
        opportunity["content"],
        opportunity["score"],
        opportunity["priority"],
        opportunity["status"],
        opportunity["date"],
        opportunity["engagement"],
        opportunity["next_steps"]
    ]
    sheet.append_row(row)
