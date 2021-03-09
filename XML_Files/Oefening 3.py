import xml.etree.ElementTree as ET
xmldoc = ET.parse("./files/jobs.xml")
root = xmldoc.getroot()

print('Overview IT vacancies:\n')
i = 1  # Purely for the format of the print function

# <editor-fold desc="Old Solution">
# for company in root.iter('company'):  # Search for tag "company"
#     company_name = company.find('name').text  # Search for tag "name" in tag "company"
#     contact = company.find('contact').find('email').text  # Search and join contact and email in "company"

#     vacancies = company.find('vacancies')  # Search for tag "vacancies" in "company"
#     for vacancy in vacancies:  # Iterate over children of tag "vacancies"
#         group = vacancy.find('position').get('group')  # Search for element "Group = IT"
#         position = vacancy.find('position').text  # Pull out tag "position"
#         if group == 'IT':  # If group = IT
#             print(str(i)+'.', '\t', "Position:", '\t', position)  # Print all information in position
#             print('\t', 'Company:', '\t', company_name)
#             print('\t', 'Contact:', '\t', contact, '\n')
#             i += 1  # Increase counter after each section
# </editor-fold>

# <editor-fold desc="New Solution">
jobs = root.find('jobs')
for company in root.find('jobs'):
    name_company = company.find('name').text
    contact_person = company.find('contact').find('email').text

    vacancies = company.find('vacancies')
    for vacancy in vacancies:
        position = vacancy.find('position')
        if position.get('group') == 'IT':
            print('{}.\tPosition:\t{}'.format(i, position.text))
            print('\tCompany:\t{}'.format(name_company))
            print('\tContact:\t{}\n'.format(contact_person))
            i += 1
# </editor-fold>