import turicreate

loaded_model = turicreate.load_model('uniformModel.model')
exec(open('trainTheMachine.py').read())
loaded_model.evaluate(sfAll, metric='all')

loaded_model.export_coreml('export' + 'Classifier.mlmodel')