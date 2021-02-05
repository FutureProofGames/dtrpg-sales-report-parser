import csv
import json
import copy


def main():
    filename = 'monthly-report.csv'
    final_report = {}
    print(filename)

    with open(filename, newline='', encoding="utf8") as salesfile:
        salesreader = csv.DictReader(salesfile)
        month_numbers = {}
        for row in salesreader:
            if not row['OrderNo'].startswith('Totals for'):
                complete_name = f"{row['Name']} - {row['Order Type']}"
                if complete_name not in month_numbers:
                    month_numbers[complete_name] = {
                        'Quantity': 0,
                        'Gross': 0.0,
                        'Net': 0.0,
                        'Fees': 0.0
                    }
                month_numbers[complete_name]['Quantity'] += int(row['Quantity'])
                month_numbers[complete_name]['Gross'] += float(row[' "Total"'])
                month_numbers[complete_name]['Net'] += float(row['Earnings'])
                month_numbers[complete_name]['Fees'] += (float(row[' "Total"']) - float(row['Earnings']))
            else:
                month = row['OrderNo'].replace('Totals for ', '')
                month = month.replace(':', '')
                final_report[month] = copy.deepcopy(month_numbers)
                month_numbers = {}

    # Calculate monthly totals
    totals_template = {
            'Gross': 0.0,
            'Net': 0.0,
            'Fees': 0.0
        }
    for month in final_report.keys():
        final_report[month]['Totals'] = copy.deepcopy(totals_template)
        # print(final_report[month].keys())

        for product in final_report[month].keys():
            if product != 'Totals':
                # print(final_report[month][product]['Gross'])
                final_report[month]['Totals']['Gross'] += final_report[month][product]['Gross']
                final_report[month]['Totals']['Net'] += final_report[month][product]['Net']
                final_report[month]['Totals']['Fees'] += final_report[month][product]['Fees']
    
    with open('parsed.json', 'w', encoding="utf8", newline='') as parsedfile:
        parsedfile.write(json.dumps(final_report))


if __name__ == "__main__":
    main()
