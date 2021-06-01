import re
# Устал мучаться с регулярками на regex'е. Прошу прощения
reg_parse = r'(^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9][01]?[0-9][0-9]?))' \
            r'.*\[(.*)\].*\"([A-Z]+)\ (\/.+?) ([\d]{1,3}) (\d+)'
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_for_parse = f.readline()
        parse = re.findall(reg_parse, line_for_parse)
        print(parse)
