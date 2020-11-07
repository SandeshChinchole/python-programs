
import random

nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']
verbs = ['Leverage', 'Sync', 'Target',
'Gamify', 'Offline', 'Crowd-sourced', '24/7', 'Lean-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed', 'B-to-B',
'Oriented', 'Cloud-based', 'API-based']

noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)

phrase = noun + ' ' + verb + ' ' + adjective

print(phrase)
