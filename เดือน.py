def get_month_name(month_number):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return "Invalid month number"
