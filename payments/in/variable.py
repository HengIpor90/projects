from bakong_khqr import KHQR 
import os
token_bakong = os.getenv("MONGODB_URI")
khqr = KHQR(token_bakong)

# create a new KHQR
bill = float(input("Enter amount (riel):"))
qr_string = khqr.create_qr(
    bank_account="hengipor_soth1@bkrt",
    merchant_name="Cafe-signal",
    merchant_city="Phnom Penh",
    amount=bill,
    currency="KHR",
    store_label="Hengpor shop",
    phone_number="012579543",
    bill_number="TRX9012211",
    terminal_label="App",
    static=True
)