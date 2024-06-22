class Agent:
    """
    Represents an agent in the swarm.

    Attributes:
        solution: The solution associated with the agent.
        name (str): The name of the agent.
    """

    def __init__(self, name=""):
        self.solution = None
        self.name = name

    def get_score(self):
        """
        Returns the score of the agent's solution.

        Returns:
            The score of the agent's solution.
        """
        return self.solution.get_score()

    def set_score(self, score):
        """
        Sets the score of the agent's solution.

        Args:
            score: The score to set.

        Raises:
            ValueError: If the agent does not have a solution yet.
        """
        if self.solution is not None:
            self.solution.set_score(score)
        else:
            raise ValueError("Agent does not have a solution yet.")

    def get_solution(self):
        """
        Returns the representation of the agent's solution.

        Returns:
            The representation of the agent's solution.
        """
        return self.solution.get_representation()
