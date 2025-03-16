########## Email Marketing Template In English ##########
import random
import pandas as pd

### Company Information
company_name = "BeYouT"

### Create Email
def create_email(f_name, l_name, age, gender, customer_type):
    ### map details into text
    temp = 0
    if age >= 15 and age <= 20:
        temp = 'youth'
    elif age <= 27:
        temp = 'middle age'
    elif age > 27:
        temp = 'others'

    age_info = {
        'youth': f"Discover our Anti-Age Booster Serum—formulated with natural ingredients to combat blemishes and boost hydration for youthful skin. ➡️ Perfect for: Tackling acne, oily skin, and maintaining a fresh, radiant look.",
        'middle age': f"Meet our Suncreen—enriched with antioxidants and SPF protection to keep your skin glowing and shielded against environmental stressors. ➡️ Perfect for: Maintaining a healthy glow while preventing early signs of aging.",
        'others': F"Elevate your skincare game with Mature Skin Care—packed with anti-aging peptides and deep hydration to reduce fine lines and restore firmness. ➡️ Perfect for: Rejuvenating and replenishing skin for a timeless appearance."
    }
    item_info = {
        'youth': 'Anti-Age Booster Serum',
        'middle age': 'Suncreen',
        'others': 'Mature Skin Care—packed'
    }
    gender_intro = {
        'M': f"Your grooming and self-care routine just got an upgrade! At {company_name}, we're passionate about helping everyone look and feel their absolute best—because confidence knows no gender.",
        'F': f"Your beauty journey is about to get a little brighter! At {company_name}, we're passionate about helping you look and feel your absolute best."
    }
    limited_offer_info = {
        'fan': f"For the next 3 days, enjoy 10% off on all {item_info[temp]}! Use code {24451} at checkout.",
        'customer': f"For the next 5 days, enjoy 15% off on all {item_info[temp]}! Use code {37541} at checkout.",
        'first time': f"For the next 7 days, enjoy 20% off on all {item_info[temp]}! Use code {45541} at checkout. \n Why Choose BeYouT? \n   -cruelty-free & vegan\n   -dermatologist-tested\n   -proven results in 4 weeks"
    }

    ### Email Template
    header = '-----------------------------The Full Email---------------------------------'
    subject_line = f"{f_name}, Discover Your Glow with {company_name}!"
    greeting = f"Hi dear {f_name} {l_name},"
    introduction = gender_intro[gender]
    main = age_info[temp]
    limited_offer = limited_offer_info[customer_type]
    Call_To_Action = f"Ready to glow? Click below to explore our collection and unlock your beauty potential!\n [CLICK BUTTON]"
    closing = f"Take the first step towards your best self, and don’t miss out on this exclusive offer! we will BE YOUr Team"
    regards = f"Warm regards, Ahura Hadipoor Digital Marketing Manager at BeYouT"
    footer = f"Follow us on BeYouT.com\n[UNSUBSCRIBE BUTTON]-if you don't like to recieve Email from us\nahurahadipoor@gmail.com"

    ### Output
    email = f"{header}\n{subject_line}\n\n{greeting}\n{introduction}\n\n{main}\n{limited_offer}\n\n{Call_To_Action}\n\n{closing}\n{regards}\n\n\n{footer}\n{header}"
    return email

### User Interface
print('What do you want?')
print('1. Make Email for random users')
print('2. Make Email for a detailed user')
choice = input('Enter your selection: ')

### Customers Detail
if choice == '1':
    count = int(input('How many Email do you want to create? '))
    df = pd.DataFrame(columns=['FirstName', 'LastName', 'Age', 'Gender', 'CustomerType', 'Email'])
    for i in range(count): 
        f_name = random.choice(['ali', 'ahmad', 'saeed', 'iman', 'mojtaba', 'ahura', 'mobina', 'narges', 'sara', 'sadra', 'yasaman', 'bita', 'mina', 'aram', 'saeedeh', 'gita', 'zahra', 'gisoo', 'aliakbar'])
        l_name = random.choice(['alipoor', 'hadipoor', 'maleki', 'habibi', 'hajipoor', 'ahmadi', 'rostami', 'hasanzad', 'farokhzad', 'mashayekh', 'nilgoon', 'mahdavi', 'karimian', 'sehat'])
        age = random.randint(15, 120)
        gender = random.choice(['M', 'F'])
        customer_type = random.choice(['fan', 'customer', 'first time'])
        email = create_email(f_name, l_name, age, gender, customer_type)

        df.loc[len(df)] = [f_name, l_name, age, gender, customer_type, email]

    df.to_csv('emails.csv', index=False)

if choice == '2':
    full_name = input("Enter Your Full Name: ")
    age = int(input("Enter Your Age: "))
    gender = input("Enter Your Gender(M/F): ")
    customer_type = input('Enter the customer type(fan, customer, first time): ')

    f_name = full_name.split()[0]
    l_name = full_name.split()[1]
    email = create_email(f_name, l_name, age, gender, customer_type)
    print(email)
    