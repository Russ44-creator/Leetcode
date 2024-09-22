# https://www.1point3acres.com/bbs/thread-1025277-1-1.html
"""
For the purposes of this interview, imagine that we own a store. This
store doesn't always have customers shopping: there might be some long
stretches of time where no customers enter the store. We've asked our
employees to write simple notes to keep track of when customers are
shopping and when they aren't by simply writing a single letter every
hour: 'Y' if there were customers during that hour, 'N' if the store
was empty during that hour.
For example, our employee might have written "Y Y N Y", which means
the store was open for four hours that day, and it had customers
shopping during every hour but its third one.
  hour: | 1 | 2 | 3 | 4 |
  log:  | Y | Y | N | Y |
           ^
           |
      No customers during hour 3
We suspect that we're keeping the store open too long, so we'd like to
understand when we *should have* closed the store. For simplicity's
sake, we'll talk about when to close the store by talking about how
many hours it was open: if our closing time is `2`, that means the
store would have been open for two hours and then closed.
  hour:     | 1 | 2 | 3 | 4 |
  log:      | Y | Y | N | Y |
  closing_time: 0   1   2   3   4
           ^              ^
           |              |
    before hour #1    after hour #4
(A closing time of 0 means we simply wouldn't have opened the store at
all that day.)
First, let's define a "penalty": what we want to know is "how bad
would it be if we had closed the store at a given hour?" For a given
log and a given closing time, we compute our penalty like this:
  +1 penalty for every hour that we're *open* with no customers
  +1 penalty for every hour that we're *closed* when customers would have shopped
For example:
  hour:    | 1 | 2 | 3 | 4 |   penalty = 3:
  log:     | Y | Y | N | Y |    (three hours with customers after closing)
penalty:  | * | * |   | * |
           ^
           |
       closing_time = 0
  hour:    | 1 | 2 | 3 | 4 |   penalty = 2:
  log:     | N | Y | N | Y |     (one hour without customers while open +
  penalty: | * |   |   | * |      one hour with customers after closing)
                       ^
                       |
                    closing_time = 2
  hour:    | 1 | 2 | 3 | 4 |   penalty = 1
  log:     | Y | Y | N | Y |     (one hour without customers while open)
  penalty: |   |   | * |   |
                           ^
                           |
                      closing_time = 4
Note that if we have a log from `n` open hours, the `closing_time`
variable can range from 0, meaning "never even opened", to n, meaning
"open the entire time".
1a)
Write a function `compute_penalty` that computes the total penalty, given
  a store log (as a space separated string) AND
  a closing time (as an integer)
In addition to writing this function, you should use tests to
demonstrate that it's correct. Do some simple testing, and then quickly
describe a few other tests you would write given more time.
## Examples
compute_penalty("Y Y N Y", 0) should return 3
compute_penalty("N Y N Y", 2) should return 2
compute_penalty("Y Y N Y", 4) should return 1
"""

# split the log into a list of Y's and N's
def compute_penalty(log: str, closing_time: int) -> int:
    log_string = log.split(" ")
    penalty = 0
    for i in range(len(log_string)):
        if i >= closing_time:
            if log_string[i] == "Y":
                penalty += 1
        elif i < closing_time:
            if log_string[i] == "N":
                penalty += 1
    return penalty
# print(compute_penalty("Y Y N Y", 0))
# print(compute_penalty("N Y N Y", 2))
# print(compute_penalty("Y Y N Y", 4))

"""
1b)
Write another function named `find_best_closing_time` that returns
the best closing time in terms of `compute_penalty` given just a
store log. You should use your answer from 1a to solve this problem.
Again, you should use tests to demonstrate that it's correct. Do
some simple testing, and then quickly describe a few other tests
you would write given more time.  
## Example
find_best_closing_time("Y Y N N") should return 2
"""
def find_best_closing_time(log: str) -> int:
    hours = log.split()
    min_penalty = float('inf')
    best_time = 0
    
    # Try closing the store at each possible time and find the one with minimum penalty
    for closing_time in range(len(hours) + 1):
        penalty = compute_penalty(log, closing_time)
        if penalty < min_penalty:
            min_penalty = penalty
            best_time = closing_time
    
    return best_time

# print(find_best_closing_time("Y Y N N"))
"""
2a)
We've asked our employees to write their store logs all together in the
same text file, marking the beginning of each day with `BEGIN` and the
end of each day as `END`, sometimes spanning multiple lines. We hoped
that the file might look like
  "BEGIN Y Y END \n BEGIN N N END"
which would represent two days, where the store was open two hours
each day. Unfortunately, our employees are often too busy to remember
to finish the logs, which means this text file is littered with
unfinished days and extra information scattered throughout. Luckily,
we know that an unbroken sequence of BEGIN, zero or more Y's or N's,
and END is going to be a valid log, so we can search the aggregate log
for those.
For example, given the aggregate log
  "BEGIN BBEGIN BEGIN N N BEGIN Y Y END N N END"
                        ^              ^
                        |              |
                        +--------------+
                            valid log

We can extract only one valid sequence, "BEGIN Y Y END". For our
purposes, we should ignore any invalid sequences. *These logs cannot
be nested.*
Write a function `get_best_closing_times` that takes an aggregate log
as a string and returns an array of best closing times for every valid
log we can find, in the order that we find them.
Again, you should use tests to demonstrate that it's correct. Do
some simple testing, and then quickly describe a few other tests
you would write given more time.
## Examples
get_best_closing_times("BEGIN Y Y END \nBEGIN N N END")
  should return an array: [2, 0]
get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END")`
  should return an array: [2]
"""

def get_best_closing_times(aggregate_log: str) -> list:
    best_closing_times = []
    start = 0

    # Remove all newline characters to clean up the log
    aggregate_log = aggregate_log.replace('\n', '')

    aggregate_logs = aggregate_log.split(" ")
    print(aggregate_logs)
    index = 0
    while index < len(aggregate_logs):
        # Find the start and end of a valid log (BEGIN ... END)
        # print(aggregate_logs[index])
        if aggregate_logs[index] == 'BEGIN':
            start = index
        else:
            index += 1
            continue
        if index == len(aggregate_logs) - 1:
            break
        index += 1
        while index < len(aggregate_logs) and aggregate_logs[index] != 'END':
            if aggregate_logs[index] == 'Y' or aggregate_logs[index] == 'N':
                index += 1
            elif aggregate_logs[index] == 'BEGIN':
                break
        if aggregate_logs[index] == 'BEGIN':
            continue
        elif aggregate_logs[index] == 'END':
            log = ' '.join(aggregate_logs[start + 1:index])
            # Extract the log between BEGIN and END
            # Find the best closing time for this log and add it to the list
            best_closing_time = find_best_closing_time(log)
            best_closing_times.append(best_closing_time)
            print(log, best_closing_time)
            index += 1
    
    return best_closing_times


print(get_best_closing_times("BEGIN Y Y END \nBEGIN N N END"))  # Output: [2, 0]
print(get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END"))  # Output: [2]