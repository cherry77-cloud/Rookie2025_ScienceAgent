from .data_agent_prompts import *
from .experiment_agent_prompts import *
from .paper_agent_prompts import *
from .laboratory_agent_prompts import *

__all__ = [
    # Data agent prompts
    'DATA_PREPARATION_DECISION_SYSTEM',
    'DATA_ANALYSIS_INSTRUCTIONS', 
    'DATASET_SUMMARY_INSTRUCTIONS',
    
    # Experiment agent prompts
    'CODE_AGENT_ROLE',
    'CODE_AGENT_GENERAL_TASK', 
    'CODE_GENERATION_RULES',
    'FIGURE_GENERATION_GUIDELINES',
    'INPUT_DATA_SUMMARY',
    'OUTPUT_FORMAT_INSTRUCTIONS',
    'FIRST_ITERATION_TASK',
    'REVISION_TASK',
    'CODE_AGENT_INSTRUCTIONS',
    'REFLECTION_AGENT_DESCRIPTION',
    'REFLECTION_AGENT_INSTRUCTIONS',
    'CODE_REWARD_AGENT_DESCRIPTION',
    'CODE_REWARD_AGENT_INSTRUCTIONS',
    
    # Paper agent prompts
    'PAPER_AGENT_SYSTEM_INTRO',
    'PAPER_FIRST_ITERATION_TASK',
    'PAPER_REVISION_TASK',
    'PAPER_AGENT_INSTRUCTIONS',
    'PAPER_REWARD_AGENT_SYSTEM',
    'PAPER_REWARD_AGENT_INSTRUCTIONS',
    
    # Laboratory agent prompts
    'PHD_LITERATURE_REVIEW_PROMPT',
    'PHD_PLAN_FORMULATION_PROMPT', 
    'PHD_RESULTS_INTERPRETATION_PROMPT',
    'PHD_LITERATURE_REVIEW_COMMANDS',
    'PHD_PLAN_FORMULATION_COMMANDS',
    'PHD_RESULTS_INTERPRETATION_COMMANDS',
    'POSTDOC_PLAN_FORMULATION_PROMPT',
    'POSTDOC_RESULTS_INTERPRETATION_PROMPT',
    'POSTDOC_PLAN_FORMULATION_COMMANDS',
    'POSTDOC_RESULTS_INTERPRETATION_COMMANDS',
    'ML_ENGINEER_DATA_PREPARATION_PROMPT',
    'ML_ENGINEER_DATA_PREPARATION_COMMANDS',
    'SW_ENGINEER_DATA_PREPARATION_PROMPT',
    'SW_ENGINEER_DATA_PREPARATION_COMMANDS'
]