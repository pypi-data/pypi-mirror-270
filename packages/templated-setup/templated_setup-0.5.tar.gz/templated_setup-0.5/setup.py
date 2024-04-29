from templated_setup import Setup_Helper

DESCRIPTION = "A quick and easy replacement for some `setup.py` implementations."

Setup_Helper.init(".templated_setup_cache.json")
Setup_Helper.setup(
	name="templated_setup",
	author="matrikater (Joel Watson)",
	description=DESCRIPTION,
	author_email="administraitor@matriko.xyz",
)
