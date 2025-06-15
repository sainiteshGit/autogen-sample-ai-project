from autogen_agentchat.agents import AssistantAgent
from azureaimodels import get_model_client
from services import (
    monitoring_diagnosis_tool,
    response_coordination_tool,
    medical_support_tool,
    administration_billing_tool,
)
from agent_domain_prompts import (
    get_monitoring_diagnosis_agent_prompt,
    get_response_coordination_agent_prompt,
    get_medical_support_agent_prompt,
    get_administration_billing_agent_prompt,
    get_planning_agent_prompt,
)


monitoring_diagnosis_agent = AssistantAgent(
    name="MonitoringDiagnosisAgent",
    model_client=get_model_client(),
    system_message=get_monitoring_diagnosis_agent_prompt(),
    description="Continuously collects and analyzes patient vitals using wearable IoT devices and historical data to detect early signs of health deterioration.",
    tools=[monitoring_diagnosis_tool],
)

response_coordination_agent = AssistantAgent(
    name="ResponseCoordinationAgent",
    model_client=get_model_client(),
    system_message=get_response_coordination_agent_prompt(),
    description="Handles alerting medical staff, scheduling appointments, managing room allocation, and dispatching transport during emergencies.",
    tools=[response_coordination_tool],
)

medical_support_agent = AssistantAgent(
    name="MedicalSupportAgent",
    model_client=get_model_client(),
    system_message=get_medical_support_agent_prompt(),
    description="Assists doctors by retrieving patient history, recommending treatments, checking medication availability, and coordinating with pharmacy systems.",
    tools=[medical_support_tool],
)

administration_billing_agent = AssistantAgent(
    name="AdministrationBillingAgent",
    model_client=get_model_client(),
    system_message=get_administration_billing_agent_prompt(),
    description="Manages insurance communication, pre-authorization, and billing workflows.",
    tools=[administration_billing_tool],
)

planning_agent = AssistantAgent(
    name="PlanningAgent",
    model_client=get_model_client(),
    system_message=get_planning_agent_prompt(),
    description="Identifies healthcare requests and delegates them to the correct agent in the MAS team.",
    tools=[],
)


def get_monitoring_diagnosis_agent() -> AssistantAgent:
    """Return the monitoring diagnosis agent."""
    return monitoring_diagnosis_agent


def get_response_coordination_agent() -> AssistantAgent:
    """Return the response coordination agent."""
    return response_coordination_agent


def get_medical_support_agent() -> AssistantAgent:
    """Return the medical support agent."""
    return medical_support_agent


def get_administration_billing_agent() -> AssistantAgent:
    """Return the administration billing agent."""
    return administration_billing_agent


def get_planning_agent() -> AssistantAgent:
    """Return the planning agent."""
    return planning_agent
