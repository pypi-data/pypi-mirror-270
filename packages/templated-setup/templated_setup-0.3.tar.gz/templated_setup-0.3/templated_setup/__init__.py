from dataclasses import dataclass as dataclass_x_dataclass
from json import load as json_x_load, dump as json_x_dump, loads as json_x_loads, dumps as json_x_dumps
from datetime import date as datetime_x_date
from time import sleep as time_x_sleep
from typing import Callable, overload
from setuptools import setup
import shutil
import sys
import os







CACHE_FILE_PATH = ""
LEGAL_NOTICE = """
==================================
Legal Notice for `templated_setup`
==================================

By using this software, you, the user, acknowledge and agree that you are solely responsible for the content that is published using this tool.
The software is provided "as is", and the developers make no representations or warranties of any kind regarding its use.

You assume all responsibility and risk for the use of this software and the materials you create or publish with it.

The developers shall not be liable for any claims, damages, or other liabilities arising from the use of the software or content published therein.

========================
THANK YOU AND TAKE CARE!
========================

"""







class Normal_People_Date:



	def __new__(cls, day_:"int", month_:"int", year_:"int") -> "datetime_x_date":
	
		return datetime_x_date(year_, month_, day_)
	
		f"[ END ] {Normal_People_Date.__new__}"



	f"[ END ]"







@dataclass_x_dataclass
class Version:



	date: 			"datetime_x_date"
	version_number: 	"str"
	notes: 			"str|None"



	def validate(self):

		is_valid, err_msg = Version.validate_version_number(self.version_number)

		if not is_valid:
			raise Exception(err_msg)

		f"[ END ] {Version.validate}"



	def repr_date(self) -> str:

		day_suffix = self.date.day

		if day_suffix == 1:
			day_suffix = "st"
		elif day_suffix == 2:
			day_suffix = "nd"
		elif day_suffix == 3:
			day_suffix = "rd"
		else:
			day_suffix = "th"

		return f"{self.date.day}{day_suffix}/{self.date.month}/{self.date.year}"
	
		f"[ END ] {Version.repr_date}"



	@staticmethod
	def validate_version_number(version_number_:"str") -> "tuple[bool,str]":
		
		s = version_number_.split(".")

		if not len(s) == 2:
			return False, "Version number must have exactly 2 parts (separated by a `.`)!"

		for i in s:
			if not i.isdigit():
				return False, "Version number must be numeric."
		
		return True, ""
	
		f"[ END ] {Version.validate_version_number}"



	f"[ END ]"







class Setup_Helper:



	###########
	# HELPERS #
	###########



	@staticmethod
	def __parse_notes(notes_:"str") -> "str":

		return "\n     |".join(notes_.split("\n"))
	
		f"[ END ] {Setup_Helper.__parse_notes}"
	


	@staticmethod
	def __init_description(readme_file_path_) -> "str":

		description = None

		if not os.path.exists(readme_file_path_):
			raise FileNotFoundError(f"No such file or directory: [{readme_file_path_}].")
		
		if not os.path.isabs(readme_file_path_):
			readme_file_path_ = os.path.abspath(readme_file_path_)

		if not os.path.isfile(readme_file_path_):
			raise FileNotFoundError(f"Expected [{readme_file_path_}] to be a file. Found a directory instead.")

		with open(readme_file_path_, "r") as f:
			description = f.read()

		if description is None:
			raise Exception(f"File [{readme_file_path_}] is empty.")

		return description
	
		f"[ END ] {Setup_Helper.__init_description}"



	@staticmethod
	def __get_answer(question:"str", satisfy_func:"Callable[[str],tuple[bool,str]]") -> "str":
		ans = ""
		while True:

			ans = input(question)
			is_valid, err_msg = satisfy_func(ans)

			if is_valid:
				break

			print(err_msg)
		
		return ans
		f"[ END ] {Setup_Helper.__get_answer}"



	@staticmethod
	def __get_y_n(question:str) -> bool:
		question = question + " (y/n) "
		while True:

			answer = input(question)

			if answer.lower() == "y":
				return True

			elif answer.lower() == "n":
				return False

			else:
				print("Please enter 'y' or 'n'.")

		return None
		f"[ END ] {Setup_Helper.__get_y_n}"



	@classmethod
	def __get_cached_data(cls):

		json_data = None

		try:
			with open(CACHE_FILE_PATH, "r") as f:
				json_data = json_x_load(f)
		except FileNotFoundError:
			with open(CACHE_FILE_PATH, "w") as f:
				json_x_dump({}, f)
			with open(CACHE_FILE_PATH, "r") as f:
				json_data = json_x_load(f)

		return json_data

		f"[ END ] {Setup_Helper.__get_cached_data}"



	@classmethod
	def __load_date(cls, override=False):

		json_data = cls.__get_cached_data()

		if not override:
			if json_data and "date" in json_data:
				cls._date_of_last_modified = datetime_x_date.fromisoformat(json_data["date"])
			else:
				cls.__inner_load_date()
		else:
			cls.__inner_load_date()

		return None

		f"[ END ] {Setup_Helper.__load_date}"



	@classmethod
	def __inner_load_date(cls):		
		do_want_to_use_current_date = Setup_Helper.__get_y_n("Would you like to use the current date?")
		json_data = cls.__get_cached_data()
		while True:
			if do_want_to_use_current_date:

				cls._date_of_last_modified = datetime_x_date.today()
				confirmed = Setup_Helper.__get_y_n(f"Is [{cls._date_of_last_modified}] Correct?")
				json_data["date"] = cls._date_of_last_modified.isoformat()
				if confirmed:
					break

			else:

				day = int(Setup_Helper.__get_answer(
					"What day was it last modified? ",
					lambda x: (x.isdigit(), "Please enter a number."))
				)

				month = int(Setup_Helper.__get_answer(
					"What month was it last modified? ",
					lambda x: (x.isdigit(), "Please enter a number."))
				)

				year = int(Setup_Helper.__get_answer(
					"What year was it last modified? ",
					lambda x: (x.isdigit(), "Please enter a number."))
				)

				try:
					cls._date_of_last_modified = datetime_x_date(year, month, day)
					confirmed = Setup_Helper.__get_y_n(f"Is [{cls._date_of_last_modified}] Correct?")
					json_data["date"] = cls._date_of_last_modified.isoformat()
					if confirmed:
						break

				except ValueError:
					print("Invalid date. Please try again.")
			
			assert isinstance(cls._date_of_last_modified, datetime_x_date)
		with open(CACHE_FILE_PATH, "w") as f:
			json_x_dump(json_data, f)
		return None
		f"[ END ] {Setup_Helper.__inner_load_date}"



	@classmethod
	def __load_version_number(cls, override=False):
		
		json_data = cls.__get_cached_data()

		if not override:
			if json_data and "version_number" in json_data:
				cls._version_number = json_data["version_number"]
			else:
				cls.__inner_load_version_number()
		else:
			cls.__inner_load_version_number()

		return None
	
		f"[ END ] {Setup_Helper.__load_version_number}"



	@classmethod
	def __inner_load_version_number(cls):
		
		while True:

			cls._version_number = Setup_Helper.__get_answer(
				"What is the version number? ",
				Version.validate_version_number
			)

			confirmed = Setup_Helper.__get_y_n(f"Is [{cls._version_number}] Correct?")
			if confirmed:
				break

		json_data = cls.__get_cached_data()
		json_data["version_number"] = cls._version_number

		with open(CACHE_FILE_PATH, "w") as f:
			json_x_dump(json_data, f)

		return None

		f"[ END ] {Setup_Helper.__inner_load_version_number}"



	@classmethod
	def __load_notes(cls, override=False):

		json_data = cls.__get_cached_data()

		if not override:
			if json_data and "notes" in json_data:
				cls._notes = json_data["notes"]
			else:
				cls.__inner_load_notes()
		else:
			cls.__inner_load_notes()

		return None

		f"[ END ] {Setup_Helper.__load_notes}"



	@classmethod
	def __inner_load_notes(cls):
		
		cls._notes = input("Enter the release notes: ")

		json_data = cls.__get_cached_data()
		json_data["notes"] = cls._notes

		with open(CACHE_FILE_PATH, "w") as f:
			json_x_dump(json_data, f)

		return None

		f"[ END ] {Setup_Helper.__inner_load_notes}"



	@classmethod
	def __load_readme_file_path(cls):
		
		json_data = cls.__get_cached_data()

		if json_data and "readme_file_path" in json_data:
			cls._readme_file_path = json_data["readme_file_path"]
		else:
			cls.__inner_load_readme_file_path()

		return None

		f"[ END ] {Setup_Helper.__load_readme_file_path}"



	@classmethod
	def __inner_load_readme_file_path(cls):

		cls._readme_file_path = input("Enter the path to the README file: ")

		json_data = cls.__get_cached_data()
		json_data["readme_file_path"] = cls._readme_file_path

		with open(CACHE_FILE_PATH, "w") as f:
			json_x_dump(json_data, f)

		return None

		f"[ END ] {Setup_Helper.__inner_load_readme_file_path}"



	@classmethod
	def __load_parameters(cls):
		if cls._is_using_pip:
			json_data = cls._json_data_when_using_pip
			cls._date_of_last_modified = datetime_x_date.fromisoformat(json_data["date"])
			cls._version_number = json_data["version_number"]
			cls._notes = json_data["notes"]
			cls._readme_file_path = json_data["readme_file_path"]
			return
		user_wants_to_change_params = False
		while True:

			if user_wants_to_change_params:
				options = [
					["Date", 		lambda: cls.__load_date(override=True)],
					["Version Number", 	lambda: cls.__load_version_number(override=True)],
					["Notes", 		lambda: cls.__load_notes(override=True)]
				]
				print("What would you like to do?")
				for i, [opt, __] in enumerate(options):
					print(f" - [{i+1}] Change {opt},")
				print(f" - {len(options)+1}] Go Back.")
				choice = int(Setup_Helper.__get_answer(
					"Enter the number of your choice: ",
					lambda x: (
						x.isdigit() and 0 < int(x) <= len(options)+1,
						"Invalid choice. Please try again.")
					)
				)
				if choice == len(options)+1:
					user_wants_to_change_params = False
					continue
				callback = options[choice-1][1]
				callback()



			cls.__load_date()
			cls.__load_version_number()
			cls.__load_notes()
			cls.__load_readme_file_path()

			print(f"\n\n")
			print(f"Date:              [{cls._date_of_last_modified}]")
			print(f"Version Number:    [{cls._version_number}]")
			print(f"Notes:             [{cls._notes}]")
			print(f"Readme File Path:  [{cls._readme_file_path}]")
			print(f"\n")

			confirmed = Setup_Helper.__get_y_n("Is this information correct?")
			if confirmed:
				break
			else:
				user_wants_to_change_params = True
				print("Please enter the information again.")


	
		f"[ END ] {Setup_Helper.__load_parameters}"



	@staticmethod
	def __clear_screen():
		if os.name == "nt":

			os.system("cls")

		else:

			os.system("clear")

		return None
		f"[ END ] {Setup_Helper.__clear_screen}"



	#################
	# INSTANTIATION #
	#################
	


	@classmethod
	def init(cls, cache_file_path_:"str") -> "None":

		global CACHE_FILE_PATH
		CACHE_FILE_PATH = cache_file_path_

		try:
			__ = cls.__activated_already
		except AttributeError:
			cls.__activated_already = None
		if cls.__activated_already:
			raise Exception("This class is a singleton and can only be activated once.")
		cls.__activated_already = True

		json_data = Setup_Helper.__get_cached_data()
		needs_update = False

		# Before uploading to PyPi, we need to hardcode the values in a source file.
		from . import _hardcoded
		with open(_hardcoded.__file__, "r") as f:
			contents = f.read()
			splitted = contents.split("\n")[1:-2]
			json_str = "\n".join(splitted)
			j_data = json_x_loads(json_str)
			if j_data != json_data:
				needs_update = True
		if needs_update:
			with open(_hardcoded.__file__, "w") as f:
				json_str = json_x_dumps(json_data, indent=4)
				f.write(f"\"\"\"\n{json_str}\n\"\"\"\n")
		with open(_hardcoded.__file__, "r") as f:
			contents = f.read()
			splitted = contents.split("\n")[1:-2]
			json_str = "\n".join(splitted)
			json_data = json_x_loads(json_str)

		assert json_data is not None

		print(" ".join(sys.argv))
		cls._is_using_pip = False
		if "egg_info" in " ".join(sys.argv):
			cls._is_using_pip = True
		if "egg-info" in " ".join(sys.argv):
			cls._is_using_pip = True
		if "setup.py bdist_wheel --dist-dir " in " ".join(sys.argv):
			cls._is_using_pip = True

		if cls._is_using_pip:
			cls._json_data_when_using_pip = json_data
			return None

		cls._date_of_last_modified = j_data.get("date", None)
		cls._version_number = j_data.get("version_number", None)
		cls._notes = j_data.get("notes", None)
		cls._readme_file_path = j_data.get("readme_file_path", None)

		return None
	
		f"[ END ] {Setup_Helper.init}"



	@classmethod
	def setup(cls, name:"str", author:"str", description:"str", **kwargs_for_setup_tools) -> "None":
		
		if not cls.__activated_already:
			raise Exception("You must call `init` before calling `setup`.")

		if not cls._is_using_pip:
			print(LEGAL_NOTICE)

		cls._name = name
		cls._author = author
		cls._description = description

		Setup_Helper.__load_parameters()
		assert isinstance(cls._date_of_last_modified, datetime_x_date)
		assert isinstance(cls._version_number, str)
		assert isinstance(cls._notes, str)
		assert isinstance(cls._readme_file_path, str)

		cls._version = Version(
			date=cls._date_of_last_modified,
			version_number=cls._version_number,
			notes=Setup_Helper.__parse_notes(cls._notes)
		)
		cls._version.validate()

		cls._finish_setup(kwargs_for_setup_tools)

		return None

		f"[ END ] {Setup_Helper.setup}"



	#################
	# JUICY METHODS #
	#################



	@classmethod
	def _finish_setup(cls, kwargs_for_setup_tools:"dict"):

		assert isinstance(cls._date_of_last_modified, datetime_x_date)
		assert isinstance(cls._version_number, str)
		assert isinstance(cls._notes, str)
		assert isinstance(cls._readme_file_path, str)

		long_description = Setup_Helper.__init_description(cls._readme_file_path)
		long_description += f"\n## V{cls._version.version_number} released on {cls._version.repr_date()}\n"
		long_description += cls._notes

		if not cls._is_using_pip:
			print(f"Current Directory: [{os.path.abspath(os.getcwd())}].")
			is_root_of_project = Setup_Helper.__get_y_n("Is this the root of the project?")
		else:
			if not os.path.exists("templated_setup.egg-info"):
				raise FileNotFoundError("The `templated_setup.egg-info` directory does not exist. Please run this script from the root of the project directory.")
			if not os.path.exists("setup.py"):
				raise FileNotFoundError("The `setup.py` file does not exist. Please run this script from the root of the project directory.")
			if not os.path.exists("templated_setup/_hardcoded.py"):
				raise FileNotFoundError("The `_hardcoded.py` file does not exist. Please run this script from the root of the project directory.")
			is_root_of_project = True

		if not is_root_of_project:
			raise Exception("This script must be run from the root of the project directory.")
		
		separator = "\\" if os.name == "nt" else "/"

		if not cls._is_using_pip:
			print(f"WARNING: ABOUT TO REMOVE THE `{os.getcwd()}{separator}dist` DIRECTORY!!")
			print("YOU HAVE 3 SECONDS TO CANCEL...")
			try:
				time_x_sleep(3)
			except KeyboardInterrupt:
				print("Cancelled.")
				exit(0)

		shutil.rmtree("dist", ignore_errors=True)

		if not cls._is_using_pip:
			cls._old_sys_argv = sys.argv
			sys.argv = [sys.argv[0], "sdist"]

		setup(
			name=cls._name,
			version=cls._version.version_number,
			author=cls._author,
			description=cls._description,
			long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",
			long_description=long_description,
			**kwargs_for_setup_tools,
		)

		if not cls._is_using_pip:
			print("\n] Setup complete.\n\n")
		else:
			return

		do_publish = Setup_Helper.__get_y_n("Would you like to publish to PyPi?")
		if not do_publish:
			exit(0)

		input("Press Enter to continue... ")
		Setup_Helper.__clear_screen()

		print(f"\tDescription is readable below...\n{long_description}")
		print()

		do_proceed = Setup_Helper.__get_y_n("Would you like to proceed?")
		if not do_proceed:
			exit(0)

		Setup_Helper.__clear_screen()
		print("WAITING 5 SECONDS.")
		print("THIS IS YOUR LAST CHANCE TO CANCEL...")
		print()
		time_x_sleep(5)

		os.system(f"{sys.executable} -m twine upload --verbose --repository pypi dist/*")

		sys.argv = cls._old_sys_argv

		return None
	
		f"[ END ] {Setup_Helper._finish_setup}"



	f"[ END ]"



