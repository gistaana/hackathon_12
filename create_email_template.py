from reminder import response
from get_encouraging_message import get_encouraging_message
from datetime import date, datetime
    
DEFAULT_MESSAGE = """
<!DOCTYPE html>
<html lang="en">
    <body>
        <h1>Congrats!</h1>
        <p>You do not have any upcomming assignments</p>
    </body>
</html>
"""

def create_email_template(name) -> str:
    """Creates an HTML email template.
    
    ! Assumes that there still exists at least 1 upcoming event, and that we're still in the Fall 2023 semester timeframe.
    
    Parameters
    -----------
    receiver: the email recipient's eamil addr, from the database
    name: the email recipient's name, from the database

    Returns
    ------------
    str: an html code of the email"""
   
    # declare variables
    today = date.today() # get today's date
    event = None # declare event dict obj that will hold the upcoming event information, in the format of the API response received from the professor's website
    
    # find the upcoming event
    for e in response["events"]:
        date_obj = datetime.strptime(e["event_date"], "%Y-%m-%d").date()
        if date_obj > today:
            event = e
            break


    if event is None:
        return DEFAULT_MESSAGE
    
    # fix the event dict fields
    date_obj = datetime.strptime(event["event_date"], "%Y-%m-%d").date() # convert date from str to datetime.date obj
    if event["class_type"] == "N/A":
        event["class_type"] == "event"

    
    # return html code for email body
    return f'''
<!DOCTYPE html>
<html>
    <body style="text-align:center;">
        <div style="margin:auto; width=50%;">
            <h2>Projects in Computer Science Fall 2023 Reminders!</h2>
            <hr>
            <p>
                Hi {name}!
                <br>A friendly reminder for an upcoming {event["class_type"]}:
            </p>
            <h3>
                {event["event_name"]}!
                <br>{date_obj.strftime("%b %d, %Y")}
                <br><span style="font-weight:normal;">{event["event_description"]}</span>
            </h3>
            <p style="font-weight:bold;"><br>~ {get_encouraging_message()} ~</p>
            <hr>
            <small>If you wish to unsubscribe to these reminders, please contact one of the creators, and we'll take your name off.
                <br>Do <b>NOT</b> reply this email! It will go nowhere!
            </small>
        </div>
    </body>
</html>
'''