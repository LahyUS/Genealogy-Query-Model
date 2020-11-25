import itertools
from fact import Fact
from unify import unify
from substitution import Substitution

def subst(facts_1, facts_2):           # Generalized Modus Ponens
   if len(facts_1) != len(facts_2):
      return False

   for f1, f2 in zip(facts_1, facts_2):
      if f1.get_predicate() != f2.get_predicate():
         return False

   return unify(facts_1, facts_2, Substitution())

def forward_chaining(kb, alpha):
   res = set()
   ## Check if alpha is proved in knowledge base
   for fact in kb.facts:
      phi = unify(fact, alpha, Substitution())
      if phi:
         if phi.empty():
            res.add('true')
            return res
         res.add(phi)

   last_generated_facts = kb.facts.copy()

   while True:
      new_facts = set()
 
      # Optimize: Incremental forward chaining
      # At iteration t, check a rule only if its premises includes at least
      # a conjunct pi that unified with the fact pi' newly inferred at iteration t - 1
      for rule_predicate in kb.rules:
         rule = kb.get_rule(rule_predicate)
         if not rule.may_triggered(last_generated_facts):
            continue

         num_premises = rule.get_num_premises()
         # Get facts that relevant to the current rule
         potential_facts = kb.get_potential_facts(rule)

         # Check if rule contains premises with the same predicate
         if not rule.dup_predicate:        
            potential_premises = itertools.combinations(sorted(potential_facts), num_premises)
         else:
            # Assumption on order of premises may failed on something like grandparent rule with two parent relations
            potential_premises = itertools.permutations(potential_facts, num_premises)


         for tuple_premises in potential_premises:
            fact_premises = [premise for premise in tuple_premises]

            # get a subtitution of kb.facts (relevant to rule) in rule premises
            theta = subst(rule.premises, fact_premises)
            if not theta:
               continue

            # subtitute theta to conclusion
            new_fact = rule.conclusion.copy()
            theta.substitute(new_fact)

            # if new fact is not a changed_name clause from a clause in kb
            if new_fact not in new_facts and new_fact not in kb.facts:
               new_facts.add(new_fact) # add new fact to fact list
               phi = unify(new_fact, alpha, Substitution()) # unify new_fact with the query
               if phi:  # if is a "true" answer or a substitution
                  if phi.empty():
                     kb.facts.update(new_facts)
                     res.add('true')
                     return res
                  res.add(phi)

      last_generated_facts = new_facts
      if not new_facts:    # if new_facts is an empty set
         if not res:       # if res is an empty set too. This mean no satisfied substitution
            res.add('false')
         return res
      kb.facts.update(new_facts)
