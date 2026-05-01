"""
Debug a class that was mostly implemented with a few missing pieces. 
It parses input data like in json format, things like a loanid, ticketid, and 
status. Based on the tickets and their status and relevant fields,
the code needs to determine whether something is fraudulen
and u had to fill in specific methods to finish the logic,
or fix logic like sorting based on a specific detail so the code works properly

What they’re testing

They want to see if you can:

Read partially written code
Understand JSON/dictionary-style data
Fill in missing class methods
Debug sorting/filtering logic
Apply rules like “fraudulent if ticket status is X”
Explain your reasoning clearly
"""

tickets = [
    {"loanId": "L1", "ticketId": "T1", "status": "open", "reason": "identity_mismatch"},
    {"loanId": "L1", "ticketId": "T2", "status": "resolved", "reason": "income_verified"},
    {"loanId": "L2", "ticketId": "T3", "status": "fraud_confirmed", "reason": "fake_docs"},
]

class FraudDetector:
    def __init__(self, tickets):
        self.tickets = tickets

    def get_tickets_for_loan(self, loan_id):
        pass

    def sort_tickets(self, tickets):
        pass

    def is_fraudulent(self, loan_id):
        pass


#SOLUTION:

class FraudDetector:
    def __init__(self, tickets):
        self.tickets = tickets

    def get_tickets_for_loan(self, loan_id):
        result = []

        for ticket in self.tickets:
            if ticket["loanId"] == loan_id:
                result.append(ticket)

        return result

    def sort_tickets(self, tickets):
        return sorted(tickets, key=lambda ticket: ticket["ticketId"])

    def is_fraudulent(self, loan_id):
        loan_tickets = self.get_tickets_for_loan(loan_id)

        for ticket in loan_tickets:
            if ticket["status"] == "fraud_confirmed":
                return True

        return False

detector = FraudDetector(tickets)
#Get tickets for one loan
print(detector.get_tickets_for_loan("L1")) #Expected: returns the 2 tickets with loanId == "L1"
# print(detector.get_tickets_for_loan("L99"))
print(detector.get_tickets_for_loan("L99")) # Expected: []
# print(detector.is_fraudulent("L2"))
print(detector.is_fraudulent("L2")) # True
#Not fraudulent loan
print(detector.is_fraudulent("L1")) #False
