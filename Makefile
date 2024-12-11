include config
include .env

test: show_day
	python $(DAY).py '$(DAY).test'


run: show_day
	python $(DAY).py '$(DAY).input'

day: 
	sed -i 's/DAY:=.*/DAY:=$(DAY)/' config
	touch $(DAY).test
	@if [ ! -f $(DAY).py ]; then cp template.py $(DAY).py; fi
	@if [ ! -f $(DAY).input ]; then make input; fi

input: show_day
	curl --cookie "session=$(SESSION)" $(URL)/day/$(DAY)/input > $(DAY).input

all: show_day input run

show_day:
	@echo "Day: $(DAY)"
all: 

