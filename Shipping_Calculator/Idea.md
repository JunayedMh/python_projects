### Extra 1. The Question: The Dynamic Shipping Calculator

You are building a pricing engine for a global shipping company. Write a program that calculates the final shipping cost based on a package's **Weight**, **Destination**, and **Delivery Speed**.

The company uses three shipping zones: `Domestic`, `Continental`, and `International`.

Here are the strict rules for pricing:

1. **Base Rates by Zone (Up to 5 kg):**
* `Domestic`: $5 flat rate.
* `Continental`: $15 flat rate.
* `International`: $30 flat rate.


2. **Heavy Package Surcharge:**
* If a package weighs **more than 5 kg**, every kilogram *above* 5 kg costs an extra $2 per kg for `Domestic` and `Continental`, and $5 per kg for `International`.


3. **Urgent Speed Premium:**
* If the speed is `"Express"`, add a **20% premium** to the entire calculated cost so far.
* If the speed is `"Overnight"`, add a **50% premium** to the entire calculated cost so far.
* Regular speed has no premium.


4. **Absolute Maximum Cap:**
* No matter how heavy or fast it is, an `International` package can **never** exceed a total cost of $200. If the math calculates more than $200, cap it exactly at $200.



**Goal:** Write the conditional logic to find the total shipping cost for a package that is **`International`**, weighs **`12 kg`**, and requests **`"Express"`** speed.

