include config

run: show_day
	python $(DAY).py

input: show_day
	curl --cookie "session=$(SESSION)" $(URL)/day/$(DAY)/input > $(DAY).txt
all: show_day input run

show_day:
	@echo "Day: $(DAY)"
all:
