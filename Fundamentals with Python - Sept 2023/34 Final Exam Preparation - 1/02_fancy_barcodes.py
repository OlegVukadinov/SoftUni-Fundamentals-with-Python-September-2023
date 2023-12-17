import re
n = int(input())

for barcode in range(n):
    text = input()

    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    match = re.findall(pattern, text)
    if match:
        text = ''.join(match)
        product_group = ''.join([x for x in text if x.isdigit()])
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
         print("Invalid barcode")