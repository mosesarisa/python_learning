def can_run_for_president(age):
    """can someone of the given age run for president in the US"""
    return age >= 35
print("Can a 20 year old run for president?", can_run_for_president(20))
print("can a 45 year old run for president?", can_run_for_president(45))
