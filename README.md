# dynalink
Dyanmic plugin system built in Python. Automatically detects plugins and checks if they are valid and do not alter the state of the system.

## How does it work?
- Uses import-time checking to ensure classes and functions meet expected criteria
- Uses metaclasses & decorators to achieve this
- Validates correctness before execution

## Future work
- extend to use within algorithmic trading framework that executes at import-time
