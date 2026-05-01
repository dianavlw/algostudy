"""
two parted question where you had to implement a class.
implement a function that rearranged a dictionary of parent to child companies 
to find topmost parent company easily, How do you optimize your workflow
"""

company_map = {
    "Affirm": ["PayBright", "Returnly"],
    "PayBright": ["SmallCo"],
    "Amazon": ["WholeFoods"]
}


def build_parent_map(company_map):
    parent_map = {}

    for parent in company_map:
        children = company_map[parent]

        for child in children:
            parent_map[child] = parent

    return parent_map



#Solution:

class CompanyHierarchy:
    def __init__(self, company_map):
        self.parent_map = self.build_parent_map(company_map)

    def build_parent_map(self, company_map):
        parent_map = {}

        for parent in company_map:
            for child in company_map[parent]:
                parent_map[child] = parent

        return parent_map

    def find_top_parent(self, company):
        while company in self.parent_map:
            company = self.parent_map[company]

        return company
    

#Given any company, find the topmost parent.
company_map = {
    "Affirm": ["PayBright", "Returnly"],
    "PayBright": ["SmallCo"],
    "Amazon": ["WholeFoods"]
}

h = CompanyHierarchy(company_map)

print(h.find_top_parent("SmallCo"))   # Affirm
print(h.find_top_parent("Returnly"))  # Affirm
print(h.find_top_parent("Affirm"))    # Affirm
print(h.find_top_parent("WholeFoods")) # Amazon

"""
“How do you optimize your workflow?”

A good interview answer:

“I optimize my workflow by first making sure I understand the requirements 
and edge cases before coding. I like to break the problem into smaller 
helper functions, write a simple working solution first, then test it 
with common and edge cases. Once it works, I look for ways to improve 
readability or efficiency. I also use Git regularly so I can make small 
commits and safely experiment.”

"""