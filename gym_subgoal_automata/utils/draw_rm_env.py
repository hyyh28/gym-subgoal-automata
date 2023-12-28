import gym
env = gym.make("gym_subgoal_automata:OfficeWorldDeliverMail-v0", params={"generation": "random", "environment_seed": 0})
auto_mata = env.get_automaton()
auto_mata.plot("./output", "OfficeWorldDeliverMail-v0.png")