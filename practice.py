import pickle

locations = {'John': 'Forest', 'Phillipa': 'Mountains', 'Pete': 'City'}

secretFile = open("secretFile2.txt", "wb")
pickle.dump(locations, secretFile)
