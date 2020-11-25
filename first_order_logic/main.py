from knowledge_base import KnowledgeBase
from fact import Fact
from sentence import Sentence

if __name__ == '__main__':

# Edit input knowledge, query and output path here
	test_number = "04"
	inp_file = 'test/' + test_number + '/knowledge.pl'
	query_file = 'test/' + test_number + '/query.pl'
	output_file = 'test/' + test_number + '/answers.txt'

	kb = KnowledgeBase()
	with open(inp_file, 'r') as f_in:
		data_base = f_in.readlines()
		KnowledgeBase.declare(kb, data_base)

	print('Done initialize knowledge base from {}.'.format(inp_file))

	with open(query_file, 'r') as f_query:
		with open(output_file, 'w') as f_out:
			for query_str in f_query.readlines():
				alpha = Fact.parse_fact(query_str)
				alpha_str = str(alpha) + '.'
				print(alpha_str)
				query_conclusion = kb.query(alpha, "backward")
				if isinstance(query_conclusion, bool):
					substs = query_conclusion.__str__()
				else: substs = list(query_conclusion)
				substs_str = ' ;\n'.join([str(subst) for subst in substs]) + '.\n'
				print(substs_str)
				f_out.write(alpha_str + '\n')
				f_out.write(substs_str + '\n')

	print('Results of queries from {} are written to {}.'.format(query_file, output_file))
