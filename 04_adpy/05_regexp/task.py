#from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

for contact in contacts_list:

    name = contact[0].split()
    if len(name) == 2:
        contact[0] = name[0]
        contact[1] = name[1]
    elif len(name) == 3:
        contact[0] = name[0]
        contact[1] = name[1]
        contact[2] = name[2]

    surname = contact[1].split()
    if len(surname) == 2:
        contact[1] = surname[0]
        contact[2] = surname[1]

    phone_number_regex = r"(\+7|8)*\s*\(*(\d{3})\)*(\s*|-*)(\d{3})(\s*|-*)(\d{2})(\s*|-*)(\d{2})"
    phone_number_subst = "+7(\\2)\\4-\\6-\\8"
    phone_number_all = re.split('\(*доб.\s*(\d+)',contact[5])
    if len(phone_number_all) > 0:
        phone_number = re.sub(phone_number_regex, phone_number_subst, phone_number_all[0])

    if len(phone_number_all) > 1:
        contact[5] = f"{phone_number} доб. {phone_number_all[1]}"
    elif len(phone_number_all) == 1:
        contact[5] = f"{phone_number}"
    else:
        contact[5] = ''

for contacts in contacts_list:
    for contact in contacts_list:
        if contacts[0] == contact[0] and contacts[1] == contact[1] and contacts != contact:
            for i in range(7):
                if contacts[i] == '' and contact[i] != '':
                    contacts[i] = contact[i]
            contacts_list.remove(contact)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)