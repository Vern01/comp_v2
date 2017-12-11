MAKEFLAGS += --silent

all:
	chmod +x main.py
	echo "run ./main.py"

clean:
	rm -rf __pycache__

fclean: clean

re: fclean all
