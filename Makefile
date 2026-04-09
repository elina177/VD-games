
install:
		uv sync

VD-games:
		uv run VD-games

build:
		uv build


package-install:
	uv tool install dist/*.whl --force
lint:
	uv run ruff check VD_games
