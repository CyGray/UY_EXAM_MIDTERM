From the scenario, it looks like we need to create a Student class with name and scores as its attributes.
There are specific rules to keep in mind when building this class:
- scores must be between 0 and 100, else an informative error (so either a custom exception or an exception
that we catch and modify the error message via print)
- Once a student record is finalized, it should be locked and immutable. Attempting to 
edit it will result in a custom exception with an informative message. So maybe once we call init once, we create a setter and
add a condition that raises this custom exception.
- Every student also needs overrides for its __str__ and __repr__

In our main flow, we should first clean our data using Pandas
- trim (we can use .str.strip())
- parse the score string into numeric values (and we need to coerce invalid values to avoid crashing the flow), so pd.to_numeric(,errors="coerce"), which will convert anything wrong to NaN instead of crashing.
- drop duplicates without including in failures list or printing
- Turn the now-cleaned rows into Student objects, with exception handling
- Every row add (batch builder) must print errors AND success
- calculate student's ave score using numpy ops

Specific class, function, and attribute names are listed in the task details.