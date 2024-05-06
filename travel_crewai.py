from crewai import Crew
from textwrap import dedent
from crewai.process import Process
import os
from langchain_groq.chat_models import ChatGroq



from src.travel_agents import TravelAgents
from src.travel_task import TravelTask




GROQ_API_KEY = os.getenv('GROQ_API_KEY')
LLM = os.getenv('LLM')

travel_agents = TravelAgents()
travel_tasks = TravelTask()

llm = ChatGroq(api_key=GROQ_API_KEY, model=LLM)

expert_travel_agent = travel_agents.expert_travel_agent()
city_selection_agent = travel_agents.city_selection_expert()
local_tour_guide = travel_agents.local_tour_guide()
travel_manager = travel_agents.travel_manager()


# print(result, end='\n\n')
# return {"messages": [AIMessage(content=result)], 'next': 'supervisor'}

# return {
#     "agent_outcome": AgentFinish(
#         return_values={
#             'output': result
#             }, 
#         log=result
#         )
#     }




if __name__ == "__main__":

    print("\n\t==== Welcome to trip planner =====",end="\n")

    input = input("\tgive a plan outline so that I can make a trip plan... ")

        
    travel_task_ = travel_tasks.travel_task(
        agent=travel_manager,
        input = input
    )
    crew = Crew(
        agents=[
            expert_travel_agent,
            city_selection_agent,
            local_tour_guide,
            travel_manager
        ],
        tasks=[
            travel_task_
        ],
        verbose=0,
        process=Process.hierarchical,
        # manager_callbacks=travel_manager,
        manager_llm=llm
    )

    result = crew.kickoff()
    print("\n\t++++++++++++++++++++++++++++++\n")
    print(result)








