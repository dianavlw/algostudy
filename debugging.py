# OOP debugging + data parsing + business rules

tickets = [
    {"loanId": "L1", "ticketId": "T1", "status": "open", "reason": "identity_mismatch"},
    {"loanId": "L1", "ticketId": "T2", "status": "resolved", "reason": "income_verified"},
    {"loanId": "L2", "ticketId": "T3", "status": "fraud_confirmed", "reason": "fake_docs"},
]

class FraudDetector:
    def __init__(self, tickets):
        self.tickets = tickets

    def get_tickets_for_loan(self, loan_id):
        # return all tickets with this loanId
        res = []

        for ticket in self.tickets:
            if ticket["loadId"] == loan_id:
                res.append(ticket)
        return res
    def sort_tickets(self, tickets):
        return tickets.sort(key=lambda ticket:ticket["ticketId"])
    
    """
        for i in range(len(tickets)):
        for j in range(i + 1, len(tickets)):
            if tickets[i]["ticketId"] > tickets[j]["ticketId"]:
                tickets[i], tickets[j] = tickets[j], tickets[i]

        return tickets
    """
    def get_latest_ticket(self, loan_id):
        # return the ticket with the highest createdAt value
        
        loan_tickets = []
        for ticket in self.tickets:
            if ticket["loanId"] == loan_id:
                loan_tickets.append(ticket)


    def is_fraudulent(self, loan_id):
        # return True if latest ticket status is "fraud_confirmed"
        loan_tickets = []
        for ticket in self.tickets:
            if ticket["loanId"] == loan_id:
                loan_tickets.append(ticket)

        for ticket in loan_tickets:
            if ticket["status"] == "fraud_confirmed":
                return True
        return False
    


#Solution

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
    

#sorting mistakes
#Bad
tickets.sort(key="ticketId")
#Good
tickets.sort(key=lambda ticket:ticket["ticketId"])

#sort by date priority
tickets.sort(key=lambda ticket:ticket["createAt"])

#descending
tickets.sort(key=lambda ticket:ticket["createdAt"], reverse= True)

