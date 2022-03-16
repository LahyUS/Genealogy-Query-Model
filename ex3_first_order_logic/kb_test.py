from sentence import Sentence
from fact import Fact
from rule import Rule
from forward_chaining import forward_chaining
from backward_chaining import backward_chaining
from substitution import Substitution
import itertools
import utils
from unify import unify

class KnowledgeBase:

   def __init__(self):
      self.facts = set()   # initialize an empty set of fact
      self.fact_predicate = dict()
      self.rules = dict()      # initialize a dictionary of rule
      self.rule_conclusion_predicate = dict()

   def add_fact(self, fact):  # method : add fact to fact set
      self.facts.add(fact)

   def add_fact_predicate(self, predicate):
      self.fact_predicate[predicate] = predicate

   def add_rule_conclusion_predicate(self, rule_conclusion_predicate):
      self.rule_conclusion_predicate[rule_conclusion_predicate] = rule_conclusion_predicate

   def add_rule(self, rule):  # method : add rule to rule list
      rule_pre = rule.conclusion.predicate
      self.rules[rule_pre] = rule

   def query(self, alpha, mode):    # method : to query
      if mode == "backward":
         query_list = []
         query_list = self.Replace(alpha)
         theta = backward_chaining(self, query_list, [])
      if mode == "forward":
         theta = forward_chaining(self, alpha)
      return theta

   def get_rule(self, rule_predicate):
      return self.rules[rule_predicate]

   def get_potential_facts(self, rule):
      facts = []
      for fact in self.facts:
         if rule.may_helpful(fact.predicate):
            facts.append(fact)
      return facts

   @staticmethod
   def declare(kb, list_data):  # initialize a knowledge database
      while list_data:
         current_line , list_data = Sentence.read_list(list_data)    # return a comment/fact/rule and update list
         type = Sentence.classify(current_line)
         if type == 'fact':
            fact = Fact.parse_fact(current_line)
            kb.add_fact(fact)
            kb.add_fact_predicate(fact.predicate)
         elif type == 'rule':
            rule = Rule.parse_rule(current_line)
            kb.add_rule(rule)
            kb.add_rule_conclusion_predicate(rule.conclusion.predicate)

   #input: alpha = father(X, harry)
   #output: queries = [male(X), parent(X, harry)].
   def Replace(self, alpha):
      query_list = []

      for i in self.facts:
          if alpha.predicate == i.predicate:
            query_list.append(alpha)
            return query_list

      if alpha.predicate in self.rules:
      # get rule of alpha
      # father -> parent, male
         rule = self.get_rule(alpha.predicate)
         num_premises = rule.get_num_premises()

         for i in range(num_premises):
            subs = Substitution()
            for j in range(len(rule.premises)):
               subs.add(rule.conclusion.args[j], alpha.args[j])
            para = rule.premises[i].copy()
            subs.substitute(para)
            query_list.append(para)
         print('my list is: ', query_list)
         return query_list


         #subs = Substitution()
         #subs = Substitution()
         # subs1.add('Parent', 'X')
         # subs2.add('Parent', 'X')
         # subs2.add('Child', 'harry_potter')
         # para1 = rule.premises[0].copy()
         # para2 = rule.premises[1].copy()
         # subs1.substitute(para1)
         # subs2.substitute(para2)
         # query_list.append(para1)
         # query_list.append(para2)