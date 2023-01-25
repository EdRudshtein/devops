import pulumi


def get_prefixed_value(n: str) -> str:
	result=f'research-{pulumi.get_stack()}-{n.strip()}'.lower()
	return result
