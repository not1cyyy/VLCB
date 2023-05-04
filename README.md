# Virtual Love Coupon Book (VLCB)
VLCB (Virtual Love Coupon Book) is a Python program that generates and sends virtual coupons for romantic activities to users via email. Users can enter their name and email address, and then either generate a random coupon code or redeem a coupon code that they have received.

# Getting Started
To use VLCB, you will need to have Python 3 and the required dependencies installed on your computer. You can install the dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

You will also need to set up a Sendinblue account and obtain an API key. You can sign up for a free account at https://app.sendinblue.com/account/register, and then obtain your API key from the API & Forms section of your account settings.

Once you have the dependencies installed and your Sendinblue API key, you can run the program by executing the following command in your terminal:

```bash
python main.py
```

This will start the program, and a window will appear where you can enter your name, email address, and coupon code.

# Generating Coupons
To generate a random coupon code, click the "Generate Coupon" button in the program window. This will generate a random coupon code for one of the following activities:

- Romantic Dinner
- Infinite Kisses
- Weekend Getaway
- Picnic Date

The coupon code will be a combination of two letters that indicate the type of activity (e.g. "RD" for Romantic Dinner) and six random alphanumeric characters (e.g. "RD5T8G").

# Redeeming Coupons
To redeem a coupon, enter your name, email address, and coupon code in the program window, and then click the "Redeem Coupon" button. This will send an email to the specified email address with the coupon code and a message indicating which activity the coupon is for.

# Logging Coupons
Every time a coupon code is sent via email, a log is added to a file called `logs.csv`. This file contains three fields for each row: the email address, the coupon code, and the timestamp when the coupon was sent.

# Contributing
If you would like to contribute to VLCB, please fork the repository and submit a pull request with your changes. You can also report any issues or suggest new features by creating an issue in the repository.

# License
VLCB is licensed under the GPL-3 License. See `LICENSE` for more information.
