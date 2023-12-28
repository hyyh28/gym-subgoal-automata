from gpt import chat_model

from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
message = prompt.format(product="colorful socks")
print(message)

Task_descriptions = {
    'MakePlank': 'MakePlank: Craft a plank using wood and a toolshed.',
    'MakeStick': 'MakeStick: Create a stick using wood and a workbench.',
    'MakeCloth': 'MakeCloth: Produce cloth from grass at a factory.',
    'MakeRope': 'MakeRope: Convert grass into rope at a toolshed.',
    'MakeShears': 'MakeShears: Combine iron and wood to make shears at a workbench, with any observation order.',
    'MakeBridge': 'MakeBridge: Assemble a bridge with iron and wood at a factory, in any observation order.',
    'GetGold': 'GetGold: Obtain gold by processing iron and wood at a factory, with a bridge built in any order.',
    'MakeBed': 'MakeBed: Manufacture a bed using wood, toolshed, grass, and workbench, observing grass before workbench.',
    'MakeAxe': 'MakeAxe: Craft an axe with wood, workbench, iron, and toolshed, observing iron before toolshed.',
    'GetGem': 'GetGem: Acquire a gem by interacting with wood, workbench, iron, toolshed, and an axe, sequencing iron before the toolshed.'
}


class CraftWorldEnvPrompt():
    def __init__(self, task_name):
        self.reward_machine_defination_description = "You are familiar with automata theory. A reward machine is " \
                                                     "defined as following: Given a set of propositional symbols " \
                                                     "$\mathcal{P}$, a set of (environment) states $S$, and a set of " \
                                                     "actions $A$, a reward machine (RM) is a tuple $R_{PSA}=<U, u_0, " \
                                                     "F, \delta_u, \delta_r>$, where $U$ is a finite set of states, " \
                                                     "$u_0 \in $ is an initial state, $F$ is a finite set of terminal " \
                                                     "states (where $U \cap F = \emptyset$, terminal states are not " \
                                                     "existed in $U$), $\delta_u$ is the state-transition function, " \
                                                     "$U \times 2^{P} \rightarrow U \cup F$, $\delta_r$ is the " \
                                                     "reward-transition function, $U \rightarrow [U \times U " \
                                                     "\rightarrow \mathcal{R}]$. A reward machine $R_{PSA}$ starts in " \
                                                     "state $u_0$, and at each subsequent time is in some state $u_t " \
                                                     "\in {U \cup F}$. At every step $t$, the machine receives as " \
                                                     "input a truth assignment $\sigma_t$, which is a set that " \
                                                     "contains exactly those propositions in $P$ that are currently " \
                                                     "true in the environment. For example, in an open door and get " \
                                                     "the key game,  $\sigma_t={e}$ if the agent open the door $e$, " \
                                                     "while $\sigma_t={k}$ if the agent get the key $k$. Then the " \
                                                     "machine moves to the next state $u_{t+1}=\delta_u(u_t, " \
                                                     "\sigma_t)$ according to the state-transition function, " \
                                                     "and outputs a reward function $r_t=\delta_r(u_t)$ according to " \
                                                     "the state-reward function. This process repeats until the " \
                                                     "machine reaches a terminal state. Note that reward machines can " \
                                                     "model never-ending tasks by defining $F = \emptyset$. "

        self.env_description = "The Craft World environment is a 2D, Minecraft-inspired world with a 39x39 " \
                               "grid, where an agent collects raw materials (wood, grass, iron) and interacts " \
                               "with tools/workstations (toolshed, workbench, factory, bridge, axe) across a " \
                               "set number of labeled locations. The goal-oriented tasks involve crafting " \
                               "items like planks, sticks, cloth, and bridges, with the agent receiving a " \
                               "reward of 1 for successful completions while moving in the four cardinal " \
                               "directions within the grid. "
        self.goal_description = "Craft a range of items within the world using distinct raw materials and " \
                                "workstations while following appropriate sequences for item interactions. "

        self.task_description = Task_descriptions[task_name]

    def few_shot_example_initization(self, path=None):

