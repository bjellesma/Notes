A virtual warehouse is a named abstraction for a massively parallet processing compute cluster and are required for DQL operations (Select), DML operations (update), and Data Loading operations (copy into)

Virtual Warehouse configuration can be changed on the fly

Virtual Warehouses contain local SSD storage used to store raw data retrieved from the storage layer

suspend warehouse - `alter warehouse my_wh suspend`. This will suspend the warehouse after current queries are finished executing

you can auto suspend a warehouse - `create warehouse my_med_wh auto_suspend=300;`. This is useful for controlling costs as it says that a warehouse can shut down after so many second.

By default, a warehouse will auto resume. We can control this by manually setting auto resume `create warehouse MY_MED_WH AUTO_RESUME=FALSE`. This may be useful if we want to not have a warehouse auto turn on.

## Billing

| Warehouse Size | Credits per Hour | Credits per Second |
|----------------|------------------|-------------------|
| **X-Small**    | 1                | 0.000278          |
| **Small**      | 2                | 0.000556          |
| **Medium**     | 4                | 0.001111          |
| **Large**      | 8                | 0.002222          |
| **X-Large**    | 16               | 0.004444          |
| **2X-Large**   | 32               | 0.008889          |
| **3X-Large**   | 64               | 0.017778          |
| **4X-Large**   | 128              | 0.035556          |
| **5X-Large**   | 256              | 0.071111          |
| **6X-Large**   | 512              | 0.142222          |

The cost of the credits will be different based on the region

| Snowflake Edition | US Regions (AWS/Azure/GCP) | Non-US Regions | Notes |
|-------------------|---------------------------|----------------|-------|
| **Standard**      | ~$2.00 - $2.50           | ~$2.50 - $3.00 | Entry-level features |
| **Enterprise**    | ~$3.00 - $3.50           | ~$3.50 - $4.00 | Multi-cluster warehouses, advanced features |
| **Business Critical** | ~$4.00 - $4.50        | ~$4.50 - $5.00 | Enhanced security, compliance features |
| **Virtual Private Snowflake** | Contact Snowflake | Contact Snowflake | Dedicated infrastructure |

If a XS Virtual Warehouse is active for 1 hour on the Standard Edition of Snowflake deployed in AWS Europe region, it will consum 1 snowflake credit and cost ~$2.50 - $3.00

### Key Billing Notes

- **Minimum charge:** 60 seconds (even if you use it for 10 seconds, you're charged for 1 minute)
- **After 60 seconds:** Billing is per-second
- **Pattern:** Each size up doubles the credit consumption and compute power

### Examples

- Start X-Small warehouse for 30 seconds → Charged 1 credit (60-second minimum)
- Start X-Small warehouse for 90 seconds → Charged for 90 seconds = 0.025 credits
