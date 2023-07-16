# item name and price
p1_name, p1_price = "datascience", 10000
p2_name, p2_price = "web", 2000
p3_name, p3_price = "logo", 200

# info about the company
company_name = "Infinitesolution"
company_address = "info@infinitesolution.com"
company_city = "Nakuru"

# message that will display at the receipt
message = "Thank you for working with us"

# This section is to create the top Border of the receipt using #
print("#" * 50)

# display the company info
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# This section is to create the top Border of the receipt using -
print("-" * 50)

# print the header for the section that will contain the items
print("\t{}\t\t ${}".format(p1_name.title(), p1_price))
print("\t{}\t\t ${}".format(p2_name.title(), p2_price))
print("\t{}\t\t ${}".format(p3_name.title(), p3_price))

# section for the total
print("=" * 50)

# calculate and print the total
Total = p1_price + p2_price + p3_price
print("\t\t Total")
print("\t\t ${}".format(Total))

# end the total section
print("=" * 50)

# display the end message
print("\n\t{}\n".format(message))

# display the bottom border of the receipt
print("*" * 50)

# The end of the program
print("It was coded on 7/12/2023 at 1:53 AM")
