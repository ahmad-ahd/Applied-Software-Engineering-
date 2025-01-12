from datetime import date

# Payment Class
class Payment:
    def __init__(self, amount, payment_date, payment_status, payment_method, transaction_id):
        self._amount = amount
        self._date = payment_date
        self._payment_status = payment_status
        self._payment_method = payment_method
        self._transaction_id = transaction_id

    def process_payment(self):
        print(f"Processing payment of {self._amount} via {self._payment_method}")

    def update_payment_status(self, status):
        self._payment_status = status
        print(f"Payment status updated to: {self._payment_status}")

    def issue_receipt(self):
        print(f"Receipt issued for transaction ID: {self._transaction_id}")

    def validate_payment(self):
        print("Validating payment details...")
        return True

    def record_transaction(self):
        print(f"Transaction {self._transaction_id} recorded successfully.")

    # Getters
    def get_payment_status(self):
        return self._payment_status

    def get_transaction_id(self):
        return self._transaction_id

# Contributor Class
class Contributor:
    def __init__(self, name, contributor_id, contributor_type, contact_info, submission_details, payment_status):
        self._name = name
        self._contributor_id = contributor_id
        self._type = contributor_type
        self._contact_info = contact_info
        self._submission_details = submission_details
        self._payment_status = payment_status

    def submit_work(self):
        print(f"{self._name} has submitted work: {self._submission_details}")

    def review_payment(self):
        print(f"Reviewing payment for {self._name}: {self._payment_status}")

    def track_payment(self):
        print(f"Tracking payment for {self._name}...")

    def request_payment(self):
        print(f"{self._name} has requested payment.")

    # Getter
    def get_payment_status(self):
        return self._payment_status

# Advert Class
class Advert:
    def __init__(self, content, size, cost, advertiser_name, duration, placement_details):
        self._content = content
        self._size = size
        self._cost = cost
        self._advertiser_name = advertiser_name
        self._duration = duration
        self._placement_details = placement_details

    def create_advert(self):
        print(f"Advert created for {self._advertiser_name}")

    def update_advert(self):
        print(f"Advert updated for {self._advertiser_name}")

    def validate_advert(self):
        print("Validating advert details...")
        return True

    def approve_advert(self):
        print(f"Advert approved for {self._advertiser_name}")

    def track_advert_performance(self):
        print(f"Tracking performance for advert of {self._advertiser_name}")

# Advertiser Class
class Advertiser:
    def __init__(self, name, advertiser_id, contact_info, advert_submissions, payment_status):
        self._name = name
        self._advertiser_id = advertiser_id
        self._contact_info = contact_info
        self._advert_submissions = advert_submissions
        self._payment_status = payment_status

    def submit_advert(self):
        print(f"{self._name} has submitted an advert.")

    def negotiate_payment(self):
        print(f"{self._name} is negotiating payment.")

    def track_payment(self):
        print(f"Tracking payment for advertiser {self._name}.")

    def request_payment(self):
        print(f"{self._name} has requested payment.")

# AccountsDepartment Class
class AccountsDepartment:
    def __init__(self):
        self.payment_list = []

    def process_payment(self, payment):
        if payment.validate_payment():
            payment.process_payment()
            payment.record_transaction()
            payment.issue_receipt()
            self.payment_list.append(payment)

    def send_payment(self, contributor):
        print(f"Sending payment to {contributor._name}")

    def invoice_advertiser(self, advertiser):
        print(f"Invoicing advertiser: {advertiser._name}")

    def initiate_legal_action(self, advertiser):
        print(f"Initiating legal action against advertiser: {advertiser._name}")

# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Command Classes
class ProcessPaymentCommand(Command):
    def __init__(self, accounts_department, payment):
        self.accounts_department = accounts_department
        self.payment = payment

    def execute(self):
        self.accounts_department.process_payment(self.payment)

class SendPaymentCommand(Command):
    def __init__(self, accounts_department, contributor):
        self.accounts_department = accounts_department
        self.contributor = contributor

    def execute(self):
        self.accounts_department.send_payment(self.contributor)

class InvoiceAdvertiserCommand(Command):
    def __init__(self, accounts_department, advertiser):
        self.accounts_department = accounts_department
        self.advertiser = advertiser

    def execute(self):
        self.accounts_department.invoice_advertiser(self.advertiser)

class LegalActionCommand(Command):
    def __init__(self, accounts_department, advertiser):
        self.accounts_department = accounts_department
        self.advertiser = advertiser

    def execute(self):
        self.accounts_department.initiate_legal_action(self.advertiser)

# Client Code
if __name__ == "__main__":
    # Create objects
    accounts_department = AccountsDepartment()
    payment = Payment(500.0, date.today(), "Pending", "Credit Card", "TXN12345")
    contributor = Contributor("Alice", 1, "Journalist", "alice@example.com", "Article on Tech", "Pending")
    advertiser = Advertiser("TechCorp", "ADV001", "contact@techcorp.com", [], "Unpaid")

    # Create commands
    process_payment_cmd = ProcessPaymentCommand(accounts_department, payment)
    send_payment_cmd = SendPaymentCommand(accounts_department, contributor)
    invoice_advertiser_cmd = InvoiceAdvertiserCommand(accounts_department, advertiser)
    legal_action_cmd = LegalActionCommand(accounts_department, advertiser)

    # Execute commands
    process_payment_cmd.execute()
    send_payment_cmd.execute()
    invoice_advertiser_cmd.execute()
    legal_action_cmd.execute()
