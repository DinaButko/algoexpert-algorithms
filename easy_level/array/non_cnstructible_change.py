def non_constructible_change(coins):
  """
  Finds the minimum amount of change that cannot be created using the given coins.

  Args:
    coins: A list of positive integers representing the values of available coins.

  Returns:
    The minimum amount of change that cannot be constructed using the given coins.
  """

  # Sort the coins in ascending order
  coins.sort()

  # Initialize the current achievable change to 0
  current_change = 0

  # Iterate through the coins
  for coin in coins:
    # If the current coin value is greater than the maximum achievable change plus 1,
    # then that amount is the minimum non-constructible change
    if coin > current_change + 1:
      return current_change + 1

    # Update the current achievable change by adding the coin value
    current_change += coin

  # If we reach the end of the loop without finding a non-constructible change,
  # it means we can create any amount of change using the given coins
  return current_change + 1