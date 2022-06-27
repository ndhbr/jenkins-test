import os.path

from mario import main

# Check if files exist
def test_exists():
	err = 'Die Datei mario.py existiert nicht'
	assert os.path.exists('mario.py'), err

# Checks if accepts negative values
def test_generate_negative(capfd, monkeypatch):
	responses = iter(['-1', '1'])
	monkeypatch.setattr('builtins.input', lambda _: next(responses))

	main()

	out, err = capfd.readouterr()
	err = 'Dein Programm darf keine negativen Werte akzeptieren'

	assert out == '#', err

# Checks if accepts 0
def test_generate_zero(capfd, monkeypatch):
	responses = iter(['0', '1'])
	monkeypatch.setattr('builtins.input', lambda _: next(responses))

	main()

	out, err = capfd.readouterr()
	err = 'Dein Programm darf den Wert 0 nicht akzeptieren'

	assert out == '#', err

# Checks if accepts 9
def test_generate_nine(capfd, monkeypatch):
	responses = iter(['9', '1'])
	monkeypatch.setattr('builtins.input', lambda _: next(responses))

	main()

	out, err = capfd.readouterr()
	err = 'Dein Programm darf den Wert 9 nicht akzeptieren'

	assert out == '#', err

# Checks pyramid with height: 1
def test_generate_one(capfd, monkeypatch):
	responses = iter(['1'])
	monkeypatch.setattr('builtins.input', lambda _: next(responses))

	main()

	out, err = capfd.readouterr()
	err = 'Deine Funktion gibt für den Wert 1 eine falsche Pyramide aus'

	assert out == '#', err

# Checks pyramid with height: 2
def test_generate_two(capfd, monkeypatch):
	responses = iter(['2'])
	monkeypatch.setattr('builtins.input', lambda _: next(responses))

	main()

	out, err = capfd.readouterr()
	err = 'Deine Funktion gibt für den Wert 2 eine falsche Pyramide aus'

	assert out == ' #\n' \
			'##', err

# Checks pyramid with height: 8
def test_generate_eight(capfd, monkeypatch):
	responses = iter(['8'])
	monkeypatch.setattr('builtins.input', lambda _: next(responses))

	main()

	out, err = capfd.readouterr()

	err = "Deine Funktion gibt für den Wert 8 eine falsche Pyramide aus"
	assert out == '       #\n' \
			'      ##\n' \
			'     ###\n' \
			'    ####\n' \
			'   #####\n' \
			'  ######\n' \
			' #######\n' \
			'########', err
