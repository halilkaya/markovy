from markov import MarkovChain

mc = MarkovChain("combine.txt")

print(mc.generate(500))
