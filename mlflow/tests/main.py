from random import randint
from mlflow.pyfunc import PythonModel
import mlflow


class MyModel(PythonModel):

	def __init__(self,seed=100):
		super().__init__()
		self.seed=seed

	def predict(self,context,model_input):
		return model_input[0]+' '+str(self.seed)


if __name__=='__main__':
	mlflow.set_tracking_uri('http://localhost:5000')
	mlflow.create_experiment('MY_EXP3')

	with mlflow.start_run():
		seed_value=randint(0,100)
		mlflow.log_param('seed',seed_value)
		model=MyModel(seed=seed_value)
		mlflow.pyfunc.log_model('my_model',python_model=model)
