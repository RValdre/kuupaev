import argparse
import csv
from datetime import date, timedelta
# Python moodul, millega on mugav navigeerida tööpäevade suhtes
from workalendar.europe import Estonia
import locale
import time


def main():

    locale.setlocale(locale.LC_TIME, "et_EE.UTF-8")

    parser = argparse.ArgumentParser(
        description='Kontrollib, kas valitud kuu 10-s päev on tööpäev')
    parser.add_argument('--year', type=int, help='Aasta, mida kontrollib')
    args = parser.parse_args()

    # Kui aasta ei ole koheselt sisestatud väärtusena, siis küsib kasutajalt aasta
    if not args.year:
        year = input("Sisesta aasta mida kontrollida: ")
        try:
            year = int(year)
        except ValueError:
            print("Viga! Palun sisesta korrektne aasta!")
            return
    else:
        year = args.year

    # Loob Eesti kalendri
    cal = Estonia()

    workdays = []

    # Loopib iga kuu 10-st päevast läbi ja kontrollib, kas see on tööpäev
    for month in range(1, 13):
        payday = date(year, month, 10)
        if cal.is_working_day(payday):
            workdays.append(payday)
        else:
            # Kui ei ole siis liigub päevi tagasi, kuni leiab esimese tööpäeva
            days_subtracted = 1
            while not cal.is_working_day(payday - timedelta(days=days_subtracted)):
                days_subtracted += 1
            date_workday = payday - timedelta(days=days_subtracted)
            workdays.append(date_workday)
    # Prindib kasutajale palgamakse päevad
    print(f"Palgamakse päevad aastal {year}:")
    for workday in workdays:
        print(f"{workday.strftime('%d. %B %Y')}")

    # Raamatupidaja meeldetuletus päevad eraldi listi.
    reminder_for_accountant = []
    for workday in workdays:
        reminder_date = workday - timedelta(days=3)
        reminder_for_accountant.append(reminder_date)

    # Kirjutame kuupäevad CSV faili
    with open(f"{year}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Ridade päised
        writer.writerow(["Palgamaksmise kuupäevad",
                        "Meeldetuletused raamatupidajale"])

        # Makse ja meeldetuletuste kuupäevad
        for workday, reminder in zip(workdays, reminder_for_accountant):
            writer.writerow([f"{workday.strftime('%d. %B %Y')}",
                            f"{reminder.strftime('%d. %B %Y')}"])


if __name__ == '__main__':
    main()
    time.sleep(10)
