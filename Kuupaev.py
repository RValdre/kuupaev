import argparse
import csv
from datetime import date, timedelta
from workalendar.europe import Estonia
import locale
import time

# Define Estonian month names
MONTHS = [
    'jaanuar',
    'veebruar',
    'märts',
    'aprill',
    'mai',
    'juuni',
    'juuli',
    'august',
    'september',
    'oktoober',
    'november',
    'detsember'
]


def main():
    locale.setlocale(locale.LC_TIME, "et_EE.UTF-8")

    parser = argparse.ArgumentParser(
        description='Kontrollib, kas valitud kuu 10-s päev on tööpäev')
    parser.add_argument('--year', type=int, help='Aasta, mida kontrollib')
    args = parser.parse_args()

    if not args.year:
        year = input("Sisesta aasta mida kontrollida: ")
        try:
            year = int(year)
        except ValueError:
            print("Viga! Palun sisesta korrektne aasta!")
            return
    else:
        year = args.year

    cal = Estonia()

    workdays = []

    for month in range(1, 13):
        payday = date(year, month, 10)
        if cal.is_working_day(payday):
            workdays.append(payday)
        else:
            days_subtracted = 1
            while not cal.is_working_day(payday - timedelta(days=days_subtracted)):
                days_subtracted += 1
            date_workday = payday - timedelta(days=days_subtracted)
            workdays.append(date_workday)

    print(f"Palgamakse päevad aastal {year}:")
    for workday in workdays:
        month_name = MONTHS[workday.month - 1]
        print(f"{workday.day}. {month_name} {workday.year}")

    reminder_for_accountant = []
    for workday in workdays:
        reminder_date = workday - timedelta(days=3)
        reminder_for_accountant.append(reminder_date)

    with open(f"{year}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Palgamaksmise kuupäevad",
                        "Meeldetuletused raamatupidajale"])

        for workday, reminder in zip(workdays, reminder_for_accountant):
            month_name = MONTHS[workday.month - 1]
            workday_str = f"{workday.day}. {month_name} {workday.year}"
            reminder_str = f"{reminder.day}. {month_name} {reminder.year}"
            writer.writerow([workday_str, reminder_str])
    print(f"CSV fail valmis !")


if __name__ == '__main__':
    main()
    time.sleep(5)
