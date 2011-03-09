# A list of all models, so I don't have to type it out over and over, and can add them as needed
def listModel():
	A = ['Device', 'Location', 'Status', 'Purchase', 'Job', 'Person', 'Esign']
	return A


def checkModel(model_name):
	list_Models = listModel()
	for model in list_Models:
		if(model_name == model):
			return True
	return False
