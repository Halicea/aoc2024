include config
include .env

run: show_day
	python $(DAY).py '$(DAY).test'

run.input: show_day
	python $(DAY).py '$(DAY).input'

input: show_day
	curl --cookie "session=$(SESSION)" $(URL)/day/$(DAY)/input > $(DAY).input

all: show_day input run

show_day:
	@echo "Day: $(DAY)"
all:
