## Simulate a simple ATM machine.
The user has a starting balance and can perform actions in a loop.

# Rules:

- Starting balance: **$1000.00**
- Menu each loop:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
- Deposit: amount must be `positive`.
- Withdraw: must be `positive` AND must not `exceed` current balance.
- If user tries to `withdraw` more than balance: print **insufficient funds**.
- All amounts must be `numeric`. Use **try/except** for invalid input.
- On **exit**, print final balance.
- After each transaction, print the **updated balance**.