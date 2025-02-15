def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    first_rows = employees.head(3)
    return first_rows
