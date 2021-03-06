import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        decider = True;
        count = len(self.facts)
        if (fact.name == "fact"):
            for i in range(0, count):
                if type(match(fact.statement, self.facts[i].statement)) is not bool:
                    decider = False
            if decider:
                self.facts.append(fact)
        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        output = []
        count = len(self.facts)
        for i in range(0, count):
            if type(match(fact.statement, self.facts[i].statement)) is not bool:
                output.append((match(fact.statement, self.facts[i].statement)))
        return output
