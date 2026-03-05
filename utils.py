from datetime import datetime

def validate_date(date_string):
    """
    Validates if the provided string matches the YYYY-MM-DD format.
    
    Args:
        date_string (str): The date string to validate.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
