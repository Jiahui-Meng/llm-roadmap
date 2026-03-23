setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip

status:
	git status --short

plan:
	@sed -n '1,220p' docs/daily-plan.md

tracker:
	@sed -n '1,260p' docs/progress-tracker.md
