# The building and running of the application uses venv & PyInstaller
# If you use any other version of Python then updating the path will be required

# Uses the libs in the venv when building the executable with PyInstaller
create:
	@echo 'Building...'
	@python3 -m PyInstaller --paths ./venv/lib/python3.9/site-packages main.py -F -n=cryptoinf
	@echo 'Build complete'

# Runs the built executable from the default output folder
run:
	@./dist/cryptoinf
