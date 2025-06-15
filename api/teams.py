from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.messages import AgentEvent, ChatMessage
from typing import Sequence
from azureaimodels import get_model_client
from agents import (
    get_monitoring_diagnosis_agent,
    get_response_coordination_agent,
    get_medical_support_agent,
    get_administration_billing_agent,
    get_planning_agent,    
)


def custom_selector_func(messages: Sequence[AgentEvent | ChatMessage]) -> str:
    planning_agent = get_planning_agent()

    if messages[-1].source != planning_agent.name:
        return planning_agent.name

    return None

def get_termination_conditions():
    """Return the termination conditions for the team chat."""

    text_termination = TextMentionTermination("TERMINATE")
    max_messages_termination = MaxMessageTermination(10)

    combined_conditions = text_termination | max_messages_termination

    return combined_conditions

monitoring_agent = get_monitoring_diagnosis_agent()
response_agent = get_response_coordination_agent()
medical_support_agent = get_medical_support_agent()
admin_agent = get_administration_billing_agent()
planning_agent = get_planning_agent()

healthcare_team = SelectorGroupChat(
    [
        planning_agent,
        response_agent,
        monitoring_agent,
        medical_support_agent,
        admin_agent,
    ],
    selector_func=custom_selector_func,
    termination_condition=get_termination_conditions(),
    model_client=get_model_client(),
    allow_repeated_speaker=True,
)

def get_healthcare_team() -> SelectorGroupChat:
    """Return the healthcare multi-agent team chat."""
    return healthcare_team