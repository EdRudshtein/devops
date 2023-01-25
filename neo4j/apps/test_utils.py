import hvac


def _initialize_vault():
	client=hvac.Client()
	#
	# print(client.is_authenticated())
	#
	client.secrets.kv.v2.create_or_update_secret(path='passwords', secret={'DB_PASSWORD':'egregregr'})


#print(create_response)
#read_response = client.secrets.kv.v2.read_secret_version(path='passwords')['data']['data']
#print(read_response)

def get_db_password() -> str:
	result=hvac.Client().secrets.kv.v2.read_secret_version(path='passwords')['data']['data']['DB_PASSWORD']
	return result
