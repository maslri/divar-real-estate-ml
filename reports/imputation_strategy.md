# Missing Value Strategy

## Dataset

Divar Real Estate Dataset

---

# 1. Structural Missing

**Definition**

A missing value that occurs because the feature is **not applicable** to that property type.

These values **must NOT be imputed**.

Example:

* `rent_value` for sale listings
* `has_pool` for apartments
* `floor` for land

---

# 2. Real Missing

**Definition**

A feature that should exist for that property type but is absent.

These values should be imputed later.

---

# Feature Imputation Strategy

| Feature                 | Valid Categories     | Structural Missing  | Real Missing | Strategy                             |
| ----------------------- | -------------------- | ------------------- | ------------ | ------------------------------------ |
| price_value             | Sell                 | Yes                 | Yes          | Impute only within sell listings     |
| rent_value              | Rent                 | Yes                 | Yes          | Impute only within rent listings     |
| credit_value            | Rent                 | Yes                 | Yes          | Impute only within rent listings     |
| rent_mode               | Rent                 | Yes                 | No           | Keep NA outside rent                 |
| credit_mode             | Rent                 | Yes                 | No           | Keep NA outside rent                 |
| rent_type               | Rent                 | Yes                 | No           | Keep NA outside rent                 |
| transformed_credit      | Rent                 | Yes                 | No           | Keep NA                              |
| transformed_rent        | Rent                 | Yes                 | No           | Keep NA                              |
| regular_person_capacity | Temporary Rent       | Yes                 | Yes          | Impute only within temporary rent    |
| extra_person_capacity   | Temporary Rent       | Yes                 | Yes          | Impute only within temporary rent    |
| property_type           | Temporary Rent       | Yes                 | No           | Keep NA outside temporary rent       |
| building_size           | Almost all           | No                  | Yes          | Median by property type/location     |
| construction_year       | Buildings            | Yes (land, presell) | Yes          | Median or model                      |
| rooms_count             | Buildings            | Yes (land)          | Yes          | Mode/Model                           |
| floor                   | Apartments & Offices | Yes                 | Very little  | Impute only for apartments/offices   |
| total_floors_count      | Apartments           | Yes                 | Yes          | Median/Mode                          |
| unit_per_floor          | Apartments           | Yes                 | Yes          | Mode                                 |
| has_elevator            | Apartments & Offices | Yes                 | Very little  | Keep NA outside valid categories     |
| has_balcony             | Apartments & Houses  | Yes                 | Moderate     | Treat separately                     |
| has_pool                | Villas               | Yes                 | Yes          | Keep NA outside villas               |
| has_sauna               | Villas               | Yes                 | Yes          | Keep NA outside villas               |
| has_jacuzzi             | Villas               | Yes                 | Yes          | Keep NA outside villas               |
| has_barbecue            | Villas               | Yes                 | Yes          | Keep NA outside villas               |
| has_security_guard      | Villas               | Yes                 | Yes          | Keep NA outside villas               |
| has_heating_system      | Residential          | Yes                 | Yes          | Mode by category                     |
| has_cooling_system      | Residential          | Yes                 | Yes          | Mode by category                     |
| has_warm_water_provider | Residential          | Yes                 | Yes          | Mode by category                     |
| has_parking             | Residential/Office   | Yes                 | Very little  | Mode/Boolean                         |
| has_warehouse           | Residential/Office   | Yes                 | Very little  | Mode/Boolean                         |
| location_latitude       | All with map         | No                  | Yes          | Do not impute blindly                |
| location_longitude      | All with map         | No                  | Yes          | Do not impute blindly                |
| neighborhood_slug       | Cities               | No                  | Yes          | Recover from coordinates if possible |

---

# Domain Rules Discovered

## Apartment

Applicable Features

* floor
* total_floors_count
* unit_per_floor
* has_elevator
* has_balcony

---

## Villa

Applicable Features

* has_pool
* has_sauna
* has_jacuzzi
* has_barbecue
* has_security_guard

---

## Residential

Applicable Features

* has_heating_system
* has_cooling_system
* has_warm_water_provider
* has_restroom

---

## Temporary Rent

Applicable Features

* regular_person_capacity
* extra_person_capacity
* cost_per_extra_person
* rent_price_on_regular_days
* rent_price_on_special_days
* rent_price_at_weekends
* property_type

---

## Sell Listings

Applicable Features

* price_value
* price_mode

---

## Rent Listings

Applicable Features

* rent_value
* credit_value
* rent_mode
* credit_mode
* rent_type

---

# General Principles

### Rule 1

Never impute Structural Missing values.

---

### Rule 2

Imputation must always be performed **inside the valid property category**, never on the whole dataset.

Example:

* `rent_value` → only rent listings
* `price_value` → only sell listings
* `floor` → only apartments

---

### Rule 3

Use domain knowledge before statistics.

A 100% missing feature is not necessarily useless; it may simply be **not applicable** for that property type.

---

### Rule 4

Preserve missing values whenever they represent **Not Applicable (N/A)** rather than **Unknown**.

---
