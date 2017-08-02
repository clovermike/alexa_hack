"""Alexa app"""

import os
from django_alexa.api import fields, intent, ResponseBuilder


ALEXA_APP_ID_DEFAULT = os.environ["ALEXA_APP_ID_DEFAULT"]
ALEXA_REQUEST_VERIFICATON = True # Enables/Disable request verification
DEBUG=True

@intent
def call_clover(session):
    """
    Call clover health

    ---

    call clover
    """
    return ResponseBuilder.create_response(message="Calling Clover Health",
                                           end_session=False,
                                           launched=True)

@intent
def benefits(session, benefit=None):
    """
    Ask clover about benefits

    ---

    clover what are my benefits
    clover tell me about my benefits
    clover tell me about my plan
    clover tell me about my {benefit} benefits
    clover tell me about my {benefit} plan
    """

    kwargs = {}
    if benefit:
        kwargs['message'] = " Here is the information about your {0} plan.".format(benefit)
        #TODO add function that will look up benefits and recite them
    else:
        kwargs['reprompt'] = "What benefits do you want to hear about?"
        # options should be all, or specific benefit keyword
    if session.get('launched'):
        kwargs['end_session'] = False
        kwargs['launched'] = session['launched']
    return ResponseBuilder.create_response(**kwargs)
