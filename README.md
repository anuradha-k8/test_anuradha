## Test Anuradha

ROI of Solar Energy

#### License

mit

### Development Details:
Customer Doctype

 - Created a custom Doctype named "Customer" with fields such as Name, Address, and Mobile Number.

 - Implemented mobile number validation to ensure proper formatting.

 - Added a child table "Monthly Energy Summary" to store monthly data:

 - Average Low Tariff (kWh), Low Tariff (₹),

 - Average High Tariff (kWh), High Tariff (₹).

 - Power Consumption Entry Doctype

Developed a Doctype named "Power Consumption Entry".

 - Users can select a Customer (linked to the Customer master), choose a Reading Timestamp, and enter Power (in kW).

 - Autonaming is handled dynamically by incrementing a count based on the customer.

 - The Tariff Type (Low/High) is auto-calculated based on the selected Reading Timestamp.

 - Energy Production (kWh) is calculated using the formula:
   Power (kW) × 0.25 (each record represents a 15-minute interval).

 - On submission, the system updates the corresponding Monthly Energy Summary for the selected customer, recalculating averages and tariffs.

Role-Based Permissions

 - Configured role permissions directly on the Doctypes.

 - Access is granted to the Sales Team and Accounts Team based on their responsibilities.



Local Setup

1. [Install Bench](https://github.com/frappe/bench).
2. Install test_anuradha app:
    ```sh
    $ bench get-app test_anuradha https://github.com/anuradha-k8/test_anuradha.git
    ```
3. Create a site with and install test_anuradha app:
    ```sh
    $ bench --site sitename.localhost install-app test_anuradha
    ```
4. Open the site in the browser:
    ```sh
    $ bench browse sitename.localhost --user Administrator
    ```
5. Access the crm page at `sitename.localhost:8000/test_anuradha` in your web browser.
