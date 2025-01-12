from datetime import date
from main import Payment, Contributor, Advertiser, AccountsDepartment, ProcessPaymentCommand, SendPaymentCommand, InvoiceAdvertiserCommand, LegalActionCommand

# Create objects
accounts_department = AccountsDepartment()

# Payment object
payment = Payment(500.0, date.today(), "Pending", "Credit Card", "TXN12345")

# Contributor object
contributor = Contributor("Alice", 1, "Journalist", "alice@example.com", "Article on Tech", "Pending")

# Advertiser object
advertiser = Advertiser("TechCorp", "ADV001", "contact@techcorp.com", [], "Unpaid")

# Create commands
process_payment_cmd = ProcessPaymentCommand(accounts_department, payment)
send_payment_cmd = SendPaymentCommand(accounts_department, contributor)
invoice_advertiser_cmd = InvoiceAdvertiserCommand(accounts_department, advertiser)
legal_action_cmd = LegalActionCommand(accounts_department, advertiser)

# Execute commands to ensure all actions are printed
process_payment_cmd.execute()
send_payment_cmd.execute()
invoice_advertiser_cmd.execute()
legal_action_cmd.execute()

# Adding tests for class methods to confirm print output
payment.process_payment()
payment.update_payment_status("Completed")
payment.issue_receipt()
payment.record_transaction()

contributor.submit_work()
contributor.review_payment()
contributor.track_payment()
contributor.request_payment()

advertiser.submit_advert()
advertiser.negotiate_payment()
advertiser.track_payment()
advertiser.request_payment()

accounts_department.process_payment(payment)
accounts_department.send_payment(contributor)
accounts_department.invoice_advertiser(advertiser)
accounts_department.initiate_legal_action(advertiser)
