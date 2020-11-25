import itertools
from fact import Fact
from unify import unify
from substitution import Substitution
import  utils

def subst(facts_1, facts_2):  # Generalized Modus Ponens
    if len(facts_1) != len(facts_2):
        return False

    for f1, f2 in zip(facts_1, facts_2):
        if f1.get_predicate() != f2.get_predicate():
            return False

    return unify(facts_1, facts_2, Substitution())

    #elif alpha.get_predicate() in kb.rule_conclusion_predicate:

new_facts = set()
def backward_chaining(kb, alpha, theta):

    # check if alpha is empty
    if len(alpha) == 0:
        return theta

    # local variable to get answer
    answer = Substitution();

    # pop a sub goal
    sub_goal = alpha.pop()

    # *********************************************************************
    # if alpha is proved in knowledge base
    # check if alpha is a fact
    if sub_goal.predicate in kb.fact_predicate:
        # if theta set is include substitutions
        if len(theta) != 0:
            satisfy_element_index = []
            sub_satisfied_theta_list = []
            # substitute these substitution onto sub_goal
            k = 0
            while k < len(theta):
                subst_value = theta[k]
                phi = sub_goal.copy()
                subst_value.substitute(phi)
                # check for if phi has a varialbe or not. Ex : "parent(X,harry_potter)."
                if utils.is_contain_variable(phi):
                    for fact in kb.facts:
                        sub_theta = unify(phi, fact, Substitution())
                        if not sub_theta:
                            continue
                        # if sub_theta is a successful substitution
                        sub_phi = phi.copy()
                        sub_theta.substitute(sub_phi)
                        if sub_phi in kb.facts:
                            if sub_theta not in sub_satisfied_theta_list:
                                sub_satisfied_theta_list.append(sub_theta)
                    k += 1

                # else, phi is a fact to check true or false
                else:
                    if phi in kb.facts:     # if sub_goal is proven in kb, then return
                        satisfy_element_index.append(k)
                    k += 1

            # add satisfied element with index in list
            if len(satisfy_element_index) != 0:
                new_theta = []
                for i in satisfy_element_index:
                    new_theta.append(theta[i])
                # update theta
                theta = new_theta
                return backward_chaining(kb, alpha, theta)

            if len(sub_satisfied_theta_list) != 0:
                theta = sub_satisfied_theta_list
            return backward_chaining(kb, alpha, theta)

        # Pre-check if current facts are enough to answer/ find a substitution for sub_goal
        count = 0
        for fact in kb.facts:
            phi = unify(fact, sub_goal, Substitution())
            if phi:
                count += 1
                if phi.empty():     # if sub_goal is proven in kb. There is no sub_goal adding. This sub_goal is done
                    return backward_chaining(kb,alpha,theta)
                else:
                    theta.append(phi)


        return backward_chaining(kb, alpha, theta)


    # *********************************************************************
    # if alpha is a rule
    if sub_goal.predicate in kb.rule_conclusion_predicate:
        # get rule of sub_goal
        rule = kb.get_rule(sub_goal.predicate)
        num_premise = rule.get_num_premises()

        # get a list contains rule's premises
        premise_list = []
        i = 0
        while i < num_premise:
            premise_list.append(rule.premises[i])
            i += 1

        conclusion = rule.conclusion
        sub_theta = unify(conclusion, sub_goal, Substitution())
        subs_value_for_premise = []
        for premise in premise_list:
            temp_premise = premise.copy()
            sub_theta.substitute(temp_premise)
            subs_val = unify(premise, temp_premise, Substitution())
            subs_value_for_premise.append(subs_val)

        i = 0
        while i < len(premise_list):
            subs_val = subs_value_for_premise[i]
            premise = premise_list[i]
            subs_val.substitute(premise)
            alpha.append(premise)
            i += 1
        return backward_chaining(kb, alpha, theta)

    #return  res