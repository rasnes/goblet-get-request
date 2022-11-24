from goblet import Goblet, goblet_entrypoint
import logging
from datetime import date

app = Goblet(
    function_name="get-test",
    routes_type="cloudrun",
    backend="cloudrun",
)
goblet_entrypoint(app)
app.log.setLevel(logging.DEBUG)  # configure goblet logger level


@app.route("/today")
@app.schedule(schedule="*/1 * * * *", timezone="Europe/Oslo")
def today():
    todays_date = str(date.today())
    logging.info(todays_date)
    # Call application logic, like functions that trigger dbt with todays_date as parameter.
    return {"date": todays_date}


@app.route("/{date}")
def date_input(date):
    # Call application logic, like functions that trigger dbt with date as parameter.
    return {"date": date}
