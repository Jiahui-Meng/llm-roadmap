lexical_score = 0.8
vector_score = 0.6
alpha = 0.5
hybrid = alpha * lexical_score + (1-alpha) * vector_score
print({'lexical': lexical_score, 'vector': vector_score, 'hybrid': hybrid})
