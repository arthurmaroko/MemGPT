
from .prompts import gpt_functions
from .prompts import gpt_system
from .agent import AgentAsync
from .utils import printd


DEFAULT = 'memgpt_chat'
DEFAULT_MODEL = 'gpt-4'

def use_preset(preset_name, persona, human, interface, persistence_manager):
    """Storing combinations of SYSTEM + FUNCTION prompts"""

    if preset_name == 'memgpt_chat':

        functions = [
            'send_message', 'pause_heartbeats',
            'core_memory_append', 'core_memory_replace',
            'conversation_search', 'conversation_search_date',
            'archival_memory_insert', 'archival_memory_search',
        ]
        available_functions = [v for k,v in gpt_functions.FUNCTIONS_CHAINING.items() if k in functions]
        printd(f"Available functions:\n", [x['name'] for x in available_functions])
        assert len(functions) == len(available_functions)

        return AgentAsync(
            model=DEFAULT_MODEL,
            system=gpt_system.get_system_text(preset_name),
            functions=available_functions,
            interface=interface,
            persistence_manager=persistence_manager,
            persona_notes=persona,
            human_notes=human,
        )

    else:
        raise ValueError(preset_name)