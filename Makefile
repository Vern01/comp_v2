MAKEFLAGS += --silent

all:
	chmod +x main.py
	python3 -m types
	echo "run ./main.py"

clean:
	rm -rf __pycache__

fclean: clean

re: fclean all
