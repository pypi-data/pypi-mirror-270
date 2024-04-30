import textwrap

from sirji_messages import AgentEnum, ActionEnum
from .base import BaseMessages


class TrainUsingSearchTermMessage(BaseMessages):

    def __init__(self):
        self.action = ActionEnum.TRAIN_USING_SEARCH_TERM.name
        self.to_agent = AgentEnum.RESEARCHER.name

        super().__init__()

    def sample(self):
        return self.generate({
            "from_agent_id": "{{Your Agent ID}}",
            "summary": "{{A concise summary to be displayed to the user for the action to be performed.}}",
            "body": textwrap.dedent("""
            Term: {{search term}}
            """)})

    def description(self):
        return "Train using a search term:"
