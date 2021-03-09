with open('./files/sponsors.txt') as file:
    sponsor_list = file.readlines()
    sponsor_list.sort()


print('Overview gifts')
print('Number\tSponsor\t\t\tAmount')

total_number_forms = 0
i = 0
field = sponsor_list[i].rstrip().split('*')

while i < len(sponsor_list):
    sponsor_id = field[0]
    total_per_sponsor = 0
    text_certificate = ''
    output = '{}\t{} {}'.format(sponsor_id, field[1], field[2])

    while i < len(sponsor_list) and field[0] == sponsor_id:
        total_per_sponsor += int(field[3])
        i += 1
        if i < len(sponsor_list):
            field = sponsor_list[i].rstrip().split('*')

    if total_per_sponsor > 40:
        total_number_forms += 1
        text_certificate = '**'

    output += '\t{}\t{}'.format(total_per_sponsor, text_certificate)
    print(output)

print('There are', total_number_forms, 'tax certificates to be sent.')
