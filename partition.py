def partition(arr):
  # number of rows
  n = len(arr)
  max_sum = sum(arr)

  # list comprehension to build dp table, + 1 so that we can reference
  # dp table by index instead of compensating for index-1

  # here the rows (i) represent the number of elements and columns (j) represent
  # whether or not it is possible to achieve a partition with the sum j
  # using only elements 0 through i inclusive in the array
  memo = [[False for j in range(max_sum+1)] for i in range(n+1)]

  # if we have any number of elements we can always achieve a sum of 0
  # with an empty partition
  for i in range(n+1):
    memo[i][0] = True

  # fill in the rest of the dp table starting at index 1, 1
  for i in range(1, n+1):
    for j in range(1, max_sum+1):
      # this means that we have seen a condition previously where it is
      # really useless to consider adding or not adding the current element

      # if we can achieve a sum with 2 elements, then there is no need to
      # check if we can with 3 elements. also if we cannot achieve that sum
      # but the current element is greater than that sum, then there is
      # still no need to check
      if arr[i-1] > j:
        memo[i][j] = memo[i-1][j]
      else:
        # here is the magic sauce

        # we are considering two possibilities, including the current element
        # and not including it

        # if we do not include it, we would just copy the value from the row
        # above us. this is done with the 'memo[i-1][j]' logic

        # however if we were to include it, in order to achieve the current sum
        # we would have to decrement by the value that we are adding. this is
        # done with the 'memo[i-1][j - arr[i-1]]' logic

        # we simply take the "better" of the two options
        memo[i][j] = memo[i-1][j] or memo[i-1][j - arr[i-1]]

  # maximum posible difference is the maximum possible sum
  difference = max_sum
  # ideal difference is max_sum // 2 (integer division)
  j = max_sum // 2
  while j >= 0:
    if memo[n][j]:
      # however many times we have had to move left, we know that
      # the partitions will mirror this movement on the right
      # so we must subtract double that distance
      difference = max_sum - 2*j
      break
    j -= 1

  # current row while navigating the table
  row = n
  # current column while navigating
  col = j

  # the partitions we will rebuild
  first_part = []
  second_part = []

  # we are always checking row above us so row must be greater than 0
  # we are only decrementing our column for every value "not included" so this
  # check is perhaps a bit redundant, but column must be non-negative
  while row > 0 and col >= 0:
    # if true above us, that indicates we included that value
    if memo[row-1][col]:
      # move up a row
      row -= 1
      # include the value at the current index in the array
      first_part.append(arr[row])
    else:
      # otherwise we didnt include it, so we move up, and decrement by
      # the value, because the new sub problem is identical to solving
      # the path for an array with a smaller maximum sum
      row -= 1
      col -= arr[row]
      second_part.append(arr[row])

  # handle output
  if difference != 0:
    out =  'Non Equal Sum. Difference is ' + str(difference) + '\n'
    out += 'Partition 1: ' + str(first_part) + '\n'
    out += 'Partition 2: ' + str(second_part)
    return out
  out = 'Equal Sum.\n'
  out += 'Partition 1: ' + str(first_part) + '\n'
  out += 'Partition 2: ' + str(second_part)
  return out


# driver
def main():
  arr = [int(x) for x in input('Array: ').split()]
  print(partition(arr))

if __name__ == '__main__':
  main()
