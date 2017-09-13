# You should implement a function here, 
#  to usefully format salaries.csv.
# For instance
#   - turn each line into its own list
#   - remove dollar signs, 
#   - convert numbers to floats.
# You will then call this function in q*.py,
#  and use the pre-formatted data, there.

def get_data(fname):

  data = []
  for line in open(fname):

    # Do stuff here...

    data.append(line)

  return data

