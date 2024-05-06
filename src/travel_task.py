
from crewai import Task
from textwrap import dedent

class TravelTask():
	def travel_task(self, agent, input):
		return Task(
			description=dedent(f"""\
				**Task**: find and provide the appropriate travel, exploration solution to the user needs.
           **Description**: you are an helpfull travel agency.    
            **Parameters**: 
            - user need: {input}"""),
			expected_output=dedent("""\
				A detailed response summarizing key findings about given context and information that could be relevant to it"""),
			# async_execution=True,
			agent=agent
		)
