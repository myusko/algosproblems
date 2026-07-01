CURRENT_DIR := $(CURDIR)

format:
	ruff format $(CURRENT_DIR)

lint:
	ruff check $(CURRENT_DIR)

test:
	python -m pytest $(CURRENT_DIR)/tests
