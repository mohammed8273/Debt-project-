# models.py

class Customer:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    def str(self):
        return f"{self.id} - {self.name} | {self.phone} | {self.address}"


class Debt:
    def __init__(self, id, customer_id, amount, date, note=""):
        self.id = id
        self.customer_id = customer_id
        self.amount = amount
        self.date = date
        self.note = note

    def str(self):
        return f"{self.id} - customer: {self.customer_id} | amount: {self.amount} | date: {self.date} | date: {self.note}"